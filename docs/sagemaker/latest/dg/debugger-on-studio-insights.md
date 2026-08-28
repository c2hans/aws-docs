---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-on-studio-insights.html
---

# Open the Amazon SageMaker Debugger Insights dashboard
<a name="debugger-on-studio-insights"></a>

**Note**
End of support notice: On June 30, 2027, AWS will end support for Amazon SageMaker Profiler. After June 30, 2027, you will no longer be able to access the Profiler console or Profiler resources. For more information, see [Profiler availability change](profiler-availability-change.md).

In the SageMaker Debugger Insights dashboard in Studio Classic, you can see the compute resource utilization, resource utilization, and system bottleneck information of your training job that runs on Amazon EC2 instances in real time and after trainings

**Note**
The SageMaker Debugger Insights dashboard runs a Studio Classic application on an `ml.m5.4xlarge` instance to process and render the visualizations. Each SageMaker Debugger Insights tab runs one Studio Classic kernel session. Multiple kernel sessions for multiple SageMaker Debugger Insights tabs run on the single instance. When you close a SageMaker Debugger Insights tab, the corresponding kernel session is also closed. The Studio Classic application remains active and accrues charges for the `ml.m5.4xlarge` instance usage. For information about pricing, see the [Amazon SageMaker Pricing](https://aws.amazon.com/sagemaker/pricing/) page.

**Important**
When you are done using the SageMaker Debugger Insights dashboard, you must shut down the `ml.m5.4xlarge` instance to avoid accruing charges. For instructions on how to shut down the instance, see [Shut down the Amazon SageMaker Debugger Insights instance](debugger-on-studio-insights-close.md).

**To open the SageMaker Debugger Insights dashboard**

1. On the Studio Classic **Home** page, choose **Experiments** in the left navigation pane.

1. Search your training job in the **Experiments** page. If your training job is set up with an Experiments run, the job should appear in the **Experiments** tab; if you didn't set up an Experiments run, the job should appear in the **Unassigned runs** tab.

1. Choose (click) the link of the training job name to see the job details.

1. Under the **OVERVIEW** menu, choose **Debuggger**. This should show the following two sections.
   + In the **Debugger rules** section, you can browse the status of the Debugger built-in rules associated with the training job.
   + In the **Debugger insights** section, you can find links to open SageMaker Debugger Insights on the dashboard.

1. In the **SageMaker Debugger Insights** section, choose the link of the training job name to open the SageMaker Debugger Insights dashboard. This opens a **Debug [your-training-job-name]** window. In this window, Debugger provides an overview of the computational performance of your training job on Amazon EC2 instances and helps you identify issues in compute resource utilization.

You can also download an aggregated profiling report by adding the built-in [ProfilerReport](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-built-in-rules.html#profiler-report) rule of SageMaker Debugger. For more information, see [Configure Built-in Profiler Rules](https://docs.aws.amazon.com/sagemaker/latest/dg/use-debugger-built-in-profiler-rules.html) and [Profiling Report Generated Using SageMaker Debugger](https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-profiling-report.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
