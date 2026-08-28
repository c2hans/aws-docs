---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/use-your-own-processing-code.html
---

# Use Your Own Processing Code
<a name="use-your-own-processing-code"></a>

You can install libraries to run your scripts in your own processing container or, in a more advanced scenario, you can build your own processing container that satisfies the contract to run in Amazon SageMaker AI. For more information about containers in SageMaker AI, see [Docker containers for training and deploying models](docker-containers.md). For a formal specification that defines the contract for an Amazon SageMaker Processing container, see [How to Build Your Own Processing Container (Advanced Scenario)](build-your-own-processing-container.md).

**Topics**
+ [Run Scripts with Your Own Processing Container](processing-container-run-scripts.md)
+ [How to Build Your Own Processing Container (Advanced Scenario)](build-your-own-processing-container.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
