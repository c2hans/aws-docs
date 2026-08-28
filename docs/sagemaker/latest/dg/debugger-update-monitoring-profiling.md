---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/debugger-update-monitoring-profiling.html
---

# Updating Debugger system monitoring and framework profiling configuration while a training job is running
<a name="debugger-update-monitoring-profiling"></a>

**Note**
End of support notice: On June 30, 2027, AWS will end support for Amazon SageMaker Profiler. After June 30, 2027, you will no longer be able to access the Profiler console or Profiler resources. For more information, see [Profiler availability change](profiler-availability-change.md).

If you want to activate or update the Debugger monitoring configuration for a training job that is currently running, use the following SageMaker AI estimator extension methods:
+ To activate Debugger system monitoring for a running training job and receive a Debugger profiling report, use the following:

  ```
  estimator.enable_default_profiling()
  ```

  When you use the `enable_default_profiling` method, Debugger initiates the default system monitoring and the `ProfileReport` built-in rule, which generates a comprehensive profiling report at the end of the training job. This method can be called only if the current training job is running without both Debugger monitoring and profiling.

  For more information, see [estimator.enable\_default\_profiling](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_train.html) in the [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable).
+ To update system monitoring configuration, use the following:

  ```
  estimator.update_profiler(
      system_monitor_interval_millis={{500}}
  )
  ```

  For more information, see [estimator.update\_profiler](https://sagemaker.readthedocs.io/en/stable/api/sagemaker_train.html) in the [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
