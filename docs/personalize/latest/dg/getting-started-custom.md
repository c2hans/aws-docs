---
source_url: https://docs.aws.amazon.com/personalize/latest/dg/getting-started-custom.html
---

# Getting started with a Custom dataset group
<a name="getting-started-custom"></a>

**Important**
In this tutorial you create a solution that uses automatic training. By default, all new solutions use automatic training. With automatic training, you incur training costs while your solution is active. To avoid unnecessary costs, make sure to delete the solution when you are finished. For more information, see [Requirements for deleting Amazon Personalize resources](deleting-resources.md).

 This getting started guide shows you how to provide personalized movie recommendations for your users with a Custom dataset group and the [User-Personalization-v2 recipe](native-recipe-user-personalization-v2.md) recipe. The tutorial uses historical data that consists of 100,000 movie ratings on 9,700 movies from 600 users.

To begin, complete the [Getting started prerequisites](gs-prerequisites.md) and then proceed to either [Getting started (console)](getting-started-console.md), [Getting started (AWS CLI)](getting-started-cli.md), [Getting started (SDK for Python (Boto3))](getting-started-python.md), or [Getting started (SDK for Java 2.x)](getting-started-java.md).

When you finish the getting started exercise, to avoid incurring unnecessary charges, delete the resources that you created. For more information, see [Requirements for deleting Amazon Personalize resources](deleting-resources.md).

**Topics**
+ [Getting started (console)](getting-started-console.md)
+ [Getting started (AWS CLI)](getting-started-cli.md)
+ [Getting started (SDK for Python (Boto3))](getting-started-python.md)
+ [Getting started (SDK for Java 2.x)](getting-started-java.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Personalize. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query personalize` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
