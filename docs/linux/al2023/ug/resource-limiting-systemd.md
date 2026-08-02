---
source_url: https://docs.aws.amazon.com/linux/al2023/ug/resource-limiting-systemd.html
---

# Limiting process resource usage in AL2023 using systemd
<a name="resource-limiting-systemd"></a>

 On Amazon Linux 2023 (AL2023), we recommend using `systemd` to control what resources can be used by processes, or groups of processes. Using `systemd` is a powerful and easy to use replacement for either manipulating `cgroups` manually, or using utilities such as [`cpulimit`](epel.md#cpulimit), which was previously only available for Amazon Linux in the third party [EPEL](epel.md) repository.

 For comprehensive information, see the upstream `systemd` documentation for [systemd.resource-control](https://www.freedesktop.org/software/systemd/man/latest/systemd.resource-control.html), or the man page for `systemd.resource-control` on an AL2023 instance.

 The examples below will use the `stress-ng` CPU stress test (from the `stress-ng` package) to simulate a CPU heavy application, and `memcached` to simulate a memory heavy application.

 The below examples cover placing a CPU limit on a one-off command and a memory limit on a service. Most resource constraints that `systemd` offers can be used in any place that `systemd` will run a process, and multiple can be used at the same time. The examples below are limited to a single constraint for illustrive purposes.

## Resource control with `systemd-run` for running one-off commands
<a name="resource-limiting-systemd-interactive"></a>

 While commonly associated with system services, `systemd` can also be used by non-root users to run services, schedule timers, or run one-off processes. In the following example, we are going to use `stress-ng` as our example application. In the first example, we will run it using `systemd-run` in the `ec2-user` default account, and in the second example we will place limits on its CPU usage.

**Example Use `systemd-run` on the command line to run a process, not limiting resource usage**

1.  Ensure the `stress-ng` package is installed, as we are going to use it for our example.

   ```
   [ec2-user ~]$ sudo dnf install -y {{stress-ng}}
   ```

1.  Use `systemd-run` to execute a 10 second CPU stress test without limiting how much CPU it can use.

   ```
   [ec2-user ~]$ systemd-run --user --tty --wait --property=CPUAccounting=1 {{stress-ng --cpu 1 --timeout 10}}
   Running as unit: run-u6.service
   Press ^] three times within 1s to disconnect TTY.
   stress-ng: info:  [339368] setting to a 10 second run per stressor
   stress-ng: info:  [339368] dispatching hogs: 1 cpu
   stress-ng: info:  [339368] successful run completed in 10.00s
   Finished with result: success
   Main processes terminated with: code=exited/status=0
   Service runtime: 10.068s
   CPU time consumed: 9.060s
   ```

    The `--user` option tells `systemd-run` to execute the command as the user we are logged in as, the `--tty` option means a TTY is attached, `--wait` means to wait until the service is finished, and the `--property=CPUAccounting=1` option instructs `systemd-run` to record how much CPU time is used running the process. The `--property` command line option can be used to pass `systemd-run` settings that could be configured in a `systemd.unit` configuration file.

 When instructed to place load on the CPU, the `stress-ng` program will use all available CPU time to perform its test for the duration you ask it to run. For a real-world application, it may be desirable to place a limit on total run-time of a process. In the below example, we will ask `stress-ng` to run for a longer time than the maximum duration restriction we place on it using `systemd-run`.

**Example Use `systemd-run` on the command line to run a process, limiting CPU usage to 1 second**

1. Ensure the `stress-ng` is installed to run this example.

1.  The `LimitCPU` property is the equivalent of `ulimit -t` which will limit the maximum amount of time on the CPU this process will be allowed to use. In this case, since we are asking for a 10 second stress run, and we are limiting the CPU usage to 1 second, the command will receive a `SIGXCPU` signal and fail.

   ```
   [ec2-user ~]$ systemd-run --user --tty --wait --property=CPUAccounting=1 --property=LimitCPU=1 {{stress-ng --cpu 1 --timeout 10}}
   Running as unit: run-u12.service
   Press ^] three times within 1s to disconnect TTY.
   stress-ng: info:  [340349] setting to a 10 second run per stressor
   stress-ng: info:  [340349] dispatching hogs: 1 cpu
   stress-ng: fail:  [340349] cpu instance 0 corrupted bogo-ops counter, 1370 vs 0
   stress-ng: fail:  [340349] cpu instance 0 hash error in bogo-ops counter and run flag, 3250129726 vs 0
   stress-ng: fail:  [340349] metrics-check: stressor metrics corrupted, data is compromised
   stress-ng: info:  [340349] unsuccessful run completed in 1.14s
   Finished with result: exit-code
   Main processes terminated with: code=exited/status=2
   Service runtime: 1.201s
   CPU time consumed: 1.008s
   ```

 More commonly, you may want to restrict the percentage of CPU time that can be consumed by a particular process. In the below example, we will restrict the percentage of CPU time that can be consumed by `stress-ng`. For a real-world service, it may be desirable to limit the maximum percentage of CPU time a background process can consume in order to leave resources free for the process serving user requests.

**Example Use `systemd-run` to limit a process to 10% of CPU time on one CPU**

1. Ensure the `stress-ng` is installed to run this example.

1.  We are going to use the `CPUQuota` property to tell `systemd-run` to constrain CPU usage for the command we are going to run. We are not limiting the amount of time the process can run for, just how much CPU it can use.

   ```
   [ec2-user ~]$ systemd-run --user --tty --wait --property=CPUAccounting=1 --property=CPUQuota=10% {{stress-ng --cpu 1 --timeout 10}}
   Running as unit: run-u13.service
   Press ^] three times within 1s to disconnect TTY.
   stress-ng: info:  [340664] setting to a 10 second run per stressor
   stress-ng: info:  [340664] dispatching hogs: 1 cpu
   stress-ng: info:  [340664] successful run completed in 10.08s
   Finished with result: success
   Main processes terminated with: code=exited/status=0
   Service runtime: 10.140s
   CPU time consumed: 1.014s
   ```

    Note how the CPU accounting tells us that while the service ran for 10 seconds, it only consumed 1 second of actual CPU time.

 There are many ways to configure `systemd` to limit resource usage for CPU, memory, networking, and IO. See the upstream `systemd` documentation for [systemd.resource-control](https://www.freedesktop.org/software/systemd/man/latest/systemd.resource-control.html), or the man page for `systemd.resource-control` on an AL2023 instance for comprehensive documentation.

 Behind the scenes, `systemd` is using features of the Linux kernel such as `cgroups` to implement these limits while avoiding the need for you to configure them by hand. The [Linux Kernel documentation for `cgroup-v2`](https://www.kernel.org/doc/html/latest/admin-guide/cgroup-v2.html) contains extensive details about `cgroups` work.

## Resource control in a `systemd` service
<a name="resource-limiting-systemd-service"></a>

 There are several parameters that can be added to the `[Service]` section of `systemd` services to control system resource usage. These include both hard and soft limits. For the exact behavior of each option, refer to the upstream `systemd` documentation for [systemd.resource-control](https://www.freedesktop.org/software/systemd/man/latest/systemd.resource-control.html), or the man page for `systemd.resource-control` on an AL2023 instance.

 Commonly used limits are `MemoryHigh` to specify a throttling limit on memory usage, `MemoryMax` to set a hard upper limit (which, once reached, the OOM Killer is invoked), and `CPUQuota` (as illustrated in the previous section). It is also possible to configure weights and priorities rather than fixed numbers.

**Example Using `systemd` to set memory usage limits on services**
 In this example we will set a hard memory usage limit for `memcached`, a simple key-value cache, and show how the OOM Killer is invoked for that service rather than the whole system.

1.  First, we need to install the packages required for this example.

   ```
   [ec2-user ~]$ sudo dnf install -y {{memcached libmemcached-awesome-tools}}
   ```

1.  Enable the `memcached.service` and then start the service so that `memcached` is running.

   ```
   [ec2-user ~]$ sudo systemctl enable {{memcached.service}}
   Created symlink /etc/systemd/system/multi-user.target.wants/memcached.service → /usr/lib/systemd/system/memcached.service.
   [ec2-user ~]$ sudo systemctl start {{memcached.service}}
   ```

1.  Check that `memcached.service` is running.

   ```
   [ec2-user ~]$ sudo systemctl status {{memcached.service}}
   ● memcached.service - memcached daemon
        Loaded: loaded (/usr/lib/systemd/system/memcached.service; enabled; preset: disabled)
        Active: active (running) since Fri 2025-01-31 22:36:42 UTC; 1s ago
      Main PID: 356294 (memcached)
         Tasks: 10 (limit: 18907)
        Memory: 1.8M
           CPU: 20ms
        CGroup: /system.slice/memcached.service
        └─356294 /usr/bin/memcached -p 11211 -u memcached -m 64 -c 1024 -l 127.0.0.1,::1

   Jan 31 22:35:36 ip-1-2-3-4.us-west-2.compute.internal systemd[1]: Started memcached.service - memcached daemon.
   ```

1.  Now that `memcached` is installed and running, we can observe that it functions by insterting some random data into the cache

    In `/etc/sysconfig/memcached` the `CACHESIZE` variable is set to 64 by default, meaning 64 megabytes. By inserting more data into the cache than the maximum cache size, we can see that we fill the cache and some items are evicted using `memcached-tool`, and that the `memcached.service` is using around 64MB of memory.

   ```
   [ec2-user ~]$ for i in $(seq 1 150); do dd if=/dev/random of=$i bs=512k count=1; memcp -s localhost $i; done
   [ec2-user ~]$ memcached-tool localhost display
     #  Item_Size  Max_age   Pages   Count   Full?  Evicted Evict_Time OOM
     2     120B         0s       1       0      no        0        0    0
    39   512.0K         4s      63     126     yes       24        2    0
   [ec2-user ~]$ sudo systemctl status {{memcached.service}}
   ● memcached.service - memcached daemon
        Loaded: loaded (/usr/lib/systemd/system/memcached.service; enabled; preset: disabled)
        Active: active (running) since Fri 2025-01-31 22:36:42 UTC; 7min ago
      Main PID: 356294 (memcached)
         Tasks: 10 (limit: 18907)
        Memory: 66.7M
           CPU: 203ms
        CGroup: /system.slice/memcached.service
                └─356294 /usr/bin/memcached -p 11211 -u memcached -m 64 -c 1024 -l 127.0.0.1,::1

   Jan 31 22:36:42 ip-1-2-3-4.us-west-2.compute.internal systemd[1]: Started memcached.service - memcached daemon.
   ```

1.  Use the `MemoryMax` property to set a hard limit for the `memcached.service` where, if hit, the OOM Killer will be invoked. Additional options can be set for the service by adding them to an override file. This can be done either by directly editing the `/etc/systemd/system/memcached.service.d/override.conf` file, or interactively using the `edit` command of `systemctl`.

   ```
   [ec2-user ~]$ sudo systemctl edit {{memcached.service}}
   ```

   Add the below to the override to set a hard limit of 32MB of memory for the service.

   ```
   [Service]
   MemoryMax=32M
   ```

1. Tell `systemd` to reload its configuration

   ```
   [ec2-user ~]$ sudo systemctl daemon-reload
   ```

1. Observe that the `memcached.service` is now running with a memory limit of 32MB.

   ```
   [ec2-user ~]$ sudo systemctl status {{memcached.service}}
   ● memcached.service - memcached daemon
        Loaded: loaded (/usr/lib/systemd/system/memcached.service; enabled; preset: disabled)
       Drop-In: /etc/systemd/system/memcached.service.d
                └─override.conf
        Active: active (running) since Fri 2025-01-31 23:09:13 UTC; 49s ago
      Main PID: 358423 (memcached)
         Tasks: 10 (limit: 18907)
        Memory: 1.8M (max: 32.0M available: 30.1M)
           CPU: 25ms
        CGroup: /system.slice/memcached.service
                └─358423 /usr/bin/memcached -p 11211 -u memcached -m 64 -c 1024 -l 127.0.0.1,::1

   Jan 31 23:09:13 ip-1-2-3-4.us-west-2.compute.internal systemd[1]: Started memcached.service - memcached daemon.
   ```

1.  The service will function normally while using less than 32MB of memory, which we can check by loading less than 32MB of random data into the cache, and then checking the status of the service.

   ```
   [ec2-user ~]$ for i in $(seq 1 30); do dd if=/dev/random of=$i bs=512k count=1; memcp -s localhost $i; done
   ```

   ```
   [ec2-user ~]$ sudo systemctl status {{memcached.service}}
   ● memcached.service - memcached daemon
        Loaded: loaded (/usr/lib/systemd/system/memcached.service; enabled; preset: disabled)
       Drop-In: /etc/systemd/system/memcached.service.d
                └─override.conf
        Active: active (running) since Fri 2025-01-31 23:14:48 UTC; 3s ago
      Main PID: 359492 (memcached)
         Tasks: 10 (limit: 18907)
        Memory: 18.2M (max: 32.0M available: 13.7M)
           CPU: 42ms
        CGroup: /system.slice/memcached.service
                └─359492 /usr/bin/memcached -p 11211 -u memcached -m 64 -c 1024 -l 127.0.0.1,::1

   Jan 31 23:14:48 ip-1-2-3-4.us-west-2.compute.internal systemd[1]: Started memcached.service - memcached daemon.
   ```

1.  We can now make `memcached` to use more than 32MB of memory by attempting to use the full 64MB of cache that the default `memcached` configuration is.

   ```
   [ec2-user ~]$ for i in $(seq 1 150); do dd if=/dev/random of=$i bs=512k count=1; memcp -s localhost $i; done
   ```

    You will observe that at some point during the above command there are connection errors to the `memcached` server. This is because the OOM Killer has killed the process due to the restriction we placed on it. The rest of the system will function as normal, and no other processes will be considered by the OOM Killer, as it is only the `memcached.service` that we have restricted.

   ```
   [ec2-user ~]$ sudo systemctl status {{memcached.service}}
   ● memcached.service - memcached daemon
        Loaded: loaded (/usr/lib/systemd/system/memcached.service; enabled; preset: disabled)
       Drop-In: /etc/systemd/system/memcached.service.d
                └─override.conf
        Active: failed (Result: oom-kill) since Fri 2025-01-31 23:20:28 UTC; 2s ago
      Duration: 2.901s
       Process: 360130 ExecStart=/usr/bin/memcached -p ${PORT} -u ${USER} -m ${CACHESIZE} -c ${MAXCONN} $OPTIONS (code=killed, signal=KILL)
      Main PID: 360130 (code=killed, signal=KILL)
           CPU: 94ms

   Jan 31 23:20:25 ip-1-2-3-4.us-west-2.compute.internal systemd[1]: Started memcached.service - memcached daemon.
   Jan 31 23:20:28 ip-1-2-3-4.us-west-2.compute.internal systemd[1]: memcached.service: A process of this unit has been killed by the OOM killer.
   Jan 31 23:20:28 ip-1-2-3-4.us-west-2.compute.internal systemd[1]: memcached.service: Main process exited, code=killed, status=9/KILL
   Jan 31 23:20:28 ip-1-2-3-4.us-west-2.compute.internal systemd[1]: memcached.service: Failed with result 'oom-kill'.
   ```
