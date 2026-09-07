---
source_url: https://docs.aws.amazon.com/whitepapers/latest/run-semiconductor-workflows-on-aws/launch-and-configure-the-entire-semiconductor-design-workflow.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Launch and configure the entire semiconductor design workflow
<a name="launch-and-configure-the-entire-semiconductor-design-workflow"></a>

 With the combination of infrastructure already in place and the guidance from the previous section, you can now launch and configure the entire workflow, to include scaling out to 10,000s of cores. We recommend using the previously mentioned AWS Solutions Implementation [Scale-Out Computing on AWS](https://aws.amazon.com/solutions/implementations/scale-out-computing-on-aws/) to launch your environment.

 The following figure shows all of the necessary resources to run your entire semiconductor design workflow on AWS. The previous section provided the details and guidance for determining what compute, storage, file systems, and networking options are required. Using [Scale-Out Computing on AWS](https://aws.amazon.com/solutions/implementations/scale-out-computing-on-aws/), you can quickly (less than an hour) launch a turnkey solution that is capable of running jobs, monitoring queues, adding users, and many other features that are advantageous to chip design workflows.

![This figure shows all of the necessary resources to run your entire semiconductor design workflow on AWS.](https://docs.aws.amazon.com/whitepapers/latest/run-semiconductor-workflows-on-aws/images/semiconductor-launch-configure-entire-workflow.png)

 **Launch and configure the entire semiconductor design workflow**

 Building on the previously launched architecture used for your POC, the environment is now extended to handle additional storage options and scaling out compute resources to 10,000s of cores.
