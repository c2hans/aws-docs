---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMechanicalTurkRequester/mturk-hits-defining-questions-web-layout.html
---

# Requester website layouts
<a name="mturk-hits-defining-questions-web-layout"></a>

If you have an existing task you created using the Mechanical Turk requester website, you can create HITs by referencing the `LayoutId` for that task and avoiding the need to provide a question value. To find the `LayoutId`, navigate to your `[Project List](https://requester.mturk.com/create/projects)` on the requester website and select the name of the project you want to use. A box pops up showing the **HIT Type ID**, **Layout ID**, and **Layout Parameters** that you can reference.

As shown in the following code example, the definition also includes the template parameters that are defined within the HTML. When you create a HIT, you need to pass both the `HITLayoutId` and values for the parameters that are defined.

```
{
  ...,
  HITLayoutId: "3O2UWD6SNTXSG9Z4I77HMZAX0U6499",
  HITLayoutParameters: [
    {
      "Name": "image_url",
      "Value": " https://my-bucket.s3.amazonaws.com/img1234.jpg "
    }
  ]
}

```

 More detail on creating HITs with these values can be found in [Creating HITs](mturk-creating-hits.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Mechanical Turk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSMechTurk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
