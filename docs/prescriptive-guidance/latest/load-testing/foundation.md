---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/load-testing/foundation.html
---

# Foundational planning for load testing
<a name="foundation"></a>

To determine the right tool and setup for the load test, be clear on why you are running the test. The following questions have to be addressed with the right type of test:
+ How much load can my application withstand?
+ Can my application handle X load?
+ Does my application automatically scale up and down?
+ Does my application behavior degrade over time with X amount of load?
+ Is my application working? (This is not a typical load test, but you can use load-testing tools to determine whether your application is functioning as expected.)

## Determine test complexity
<a name="complexity"></a>

Test complexity is determined by how complete your evaluation will be. Basic tools, such as [Hey](https://github.com/rakyll/hey) or [ab](https://httpd.apache.org/docs/2.4/programs/ab.html), can run requests against a single application URI. These tools are the most efficient ones, but they test only one aspect of your application. In some cases, this can be sufficient. For example, if you want to test scaling, it is sufficient to make calls against an endpoint to inflict load in the dimension you want to test. For example, the CPU load can be a huge payload or an intensive calculation that creates CPU load. If you have a distributed system, you might want to invoke an endpoint that starts a complex and distributed process.

In other cases, you might need the test to perform a complex behavior. For example, you need to log in before starting a process, or you are testing an order process that includes selecting an item and performing the purchase. This can be understood as a scenario. Testing scenarios requires more complex load-testing tools where you can shape the workload to match real-life situations. This will yield results that you can use to make assertions about the performance that end users will experience.

Complex tests induce more load on the load-generating system. For running load tests, you must consider not only the tool but also the system that runs the tool, its CPU and network bandwidth being the most important aspects. A badly designed load test computer system can lead to wrong results. For example, a single machine will not be sufficient to create load for a well-performing target. In this case, you must set up a distributed load test. On the other hand, a well-performing tool can create more load with a single server. This will be covered in greater depth in the discussion of test setup.

## Measurement and setup
<a name="measurement"></a>

Representability of the test environment must be considered. If you are running a huge shopping site, with thousands of servers, it can become difficult to test production without affecting end users or to create a test environment that replicates the site's size. In addition, creating sufficient traffic to put stress on system with this scale also requires a sophisticated load test setup. For this reason, load tests are usually run on smaller, comparable setups that you can use to draw assumptions about the production environment. Tests that establish baselines or functional requirements can be run on production environments.

It's a good practice to document test environments for subsequent tests so that you have a well-defined specification, with which results to expect for which size of target environment.

Consider all elements of the infrastructure that are affected by the load test. While the test is often looking at the CPU and memory of the hosts, there are other side effects that are relevant to consider.

A typical side effect is that the network bandwidth for communication between your services can reach its limits. For services that are connected through the internet or for distributed systems, the communication is usually based on a network. Using a load test that creates stress on the application will also create stress on the underlying network infrastructure.

## Load modeling and stepped tests
<a name="modeling"></a>

For different tests, you can model how much load is produced over the course of the test. A basic way is to create a stepped progression that will gradually increase the load over time. This will create distinct data points for every step, which enables you to draw more detailed conclusions which a single test run. To find a limit that is relevant for your application, it's a good practice to start the test with a load that's below the typical usage where you will expect top performance. When you gradually increase the load, you will see the limit where application performance is degrading. Results will show if expected behavior is still valid and that your application behaves as expected in faulty situations. For example, when testing above the limit, you could expect your application to [shed load](https://medium.com/helpshift-engineering/load-shedding-in-web-services-9fa8cfa1ffe4).

Using complex tools, you can set up a pattern as a configuration for your test. This will define how much load will be produced for a period and how it will increase or decrease.

Most of the basic tools are command line tools, which require you to script a solution yourself. When you write your own scripts, make sure that you are not accidentally overwriting metrics you want to keep. Output files should have new suffixes for each iteration, so that you don't overwrite the results of your previous iteration.
