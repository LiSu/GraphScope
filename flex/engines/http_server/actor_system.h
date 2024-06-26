/** Copyright 2020 Alibaba Group Holding Limited.
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 * 	http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#ifndef ENGINES_HTTP_SERVER_ACTOR_SYSTEM_H_
#define ENGINES_HTTP_SERVER_ACTOR_SYSTEM_H_

#include <semaphore.h>
#include <atomic>
#include <cstdint>
#include <functional>
#include <memory>
#include <thread>

namespace server {

class actor_system {
 public:
  actor_system(
      uint32_t num_shards, bool enable_dpdk,
      bool enable_thread_resource_pool = false,
      unsigned external_thread_num = 1, std::function<void()> on_exit = []() {})
      : num_shards_(num_shards),
        enable_dpdk_(enable_dpdk),
        enable_thread_resource_pool_(enable_thread_resource_pool),
        external_thread_num_(external_thread_num),
        on_exit_(on_exit) {}
  ~actor_system();

  void launch();
  void terminate();

 private:
  void launch_worker();

 private:
  const uint32_t num_shards_;
  const bool enable_dpdk_;
  const bool enable_thread_resource_pool_;
  const unsigned external_thread_num_;
  std::function<void()> on_exit_;
  std::unique_ptr<std::thread> main_thread_;
  std::atomic<bool> running_{false};
  sem_t ready_;
};

}  // namespace server

#endif  // ENGINES_HTTP_SERVER_ACTOR_SYSTEM_H_
