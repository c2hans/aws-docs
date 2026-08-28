---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_HITLayoutArticle.html
---

# HITLayout
<a name="ApiReference_HITLayoutArticle"></a>

**Topics**
+ [Description](#ApiReference_HITLayoutArticle-description)
+ [Obtaining a Layout ID](#ApiReference_HITLayoutArticle-creatingHITlayoutId)
+ [Using a HITLayout](#ApiReference_HITLayoutArticle-usingaHITlayoutId)
+ [Guidelines for Using HITLayouts](#ApiReference_HITLayoutArticle-guidelines-for-using-HITLayout-questions)

## Description
<a name="ApiReference_HITLayoutArticle-description"></a>

A HITLayout is a reusable Amazon Mechanical Turk project template used to provide Human Intelligence Task (HIT) question data for `CreateHIT`. You can create a HITLayout template by creating a Mechanical Turk project on the [Amazon Mechanical Turk Requester website](https://requester.mturk.com/create/projects/new). For more information about creating a project, see [How to Create a Project](http://docs.aws.amazon.com/AWSMechTurk/latest/RequesterUI/CreatingaHITTemplate.html) in the [Requester UI Guide](http://docs.aws.amazon.com/AWSMechTurk/latest/RequesterUI/).

## Obtaining a Layout ID
<a name="ApiReference_HITLayoutArticle-creatingHITlayoutId"></a>

A **Layout ID** is assigned to each Mechanical Turk project you create on the Requester website. You use the **Layout ID** as the value for `HITLayoutId` when calling `CreateHIT` to identify the HITLayout project template to use. Mechanical Turk projects can contain parameter placeholders in the format `${parameter_name}`. The names for the parameter placeholders used in a HITLayout project template are listed as **Parameters** along with the **Layout ID** on the Requester website.

**To view the Layout ID and the Parameters used in your HITLayout project template**

1.  Go to the [Amazon Mechanical Turk Requester website](https://requester.mturk.com/). Or for the Requester Sandbox site, go to the [Amazon Mechanical Turk Requester Sandbox website](https://requestersandbox.mturk.com/).

1.  Click **Create**, and then click **New Batch with an Existing Project**.

1.  Click the **Project Name** of an existing project to view **Layout ID** and **Parameters**.
![Click Project Name to View LayoutID](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/images/AWS-Mturk-Existing-Projects-LayoutId-01.jpg)

## Using a HITLayout
<a name="ApiReference_HITLayoutArticle-usingaHITlayoutId"></a>

You can use the HITLayout form of a HIT by calling `CreateHIT` with a `HITLayoutId` and a list of [HITLayoutParameter](ApiReference_HITLayoutParameterArticle.md) structures. The project parameter placeholders are replaced with values from the [HITLayoutParameter](ApiReference_HITLayoutParameterArticle.md) structures when you call `CreateHIT` to create a HIT. You need one structure for each of the parameter values you want substituted. The parameter names that you pass to `CreateHIT` must match the parameter names used in the HITLayout project template created on the Requester website. The parameter values cannot be changed after the HIT has been created.

**Note**
You can use either the `HITLayoutId` or the `Question` parameter when calling `CreateHIT`, but not both.

Each `CreateHIT` call merges the parameter values from HITLayoutParameter structures into the HITLayout template to generate the HIT question document. You use the same **Layout ID** in `HITLayoutId` to call `CreateHIT` multiple times, with different parameter values supplied each time for the placeholders.

Requesters can use this parameter substitution capability to create a large number of HITs that all share a common design. For example, you can create a HIT question that asks Workers to provide keywords for an image and draw boxes around key image features using a JavaScript library. First, you use the Requester website to create a Mechanical Turk project that uses a parameter placeholder for the image URL. Then you call `CreateHIT` using the same HITLayout template iteratively, using a different image URL value each time. Each call to `CreateHIT` uses the same **Layout ID**, but each call uses a different HITLayoutParameter structure that contains a unique image URL.

## Guidelines for Using HITLayouts
<a name="ApiReference_HITLayoutArticle-guidelines-for-using-HITLayout-questions"></a>
+ After a HIT is created, the HIT behaves like an HTMLQuestion HIT, which gives you the option to use HTML and JavaScript features in your HIT design, including Asynchronous JavaScript and XML (AJAX) callbacks.
+ Parameter substitution allows you to replace a short parameter name with long strings of text. You will receive errors if the resulting document is longer than permitted by the `Question` parameter of `CreateHIT`.
+ The HITLayout is used to create an HTMLQuestion document. HITLayoutParameter values with reserved characters or invalid HTML markup may result in an invalid HTMLQuestion document. For more information, see [HTMLQuestion](ApiReference_HTMLQuestionArticle.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Mechanical Turk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSMechTurk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
