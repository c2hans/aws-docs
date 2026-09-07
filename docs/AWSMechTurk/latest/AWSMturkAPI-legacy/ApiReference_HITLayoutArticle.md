---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_HITLayoutArticle.html
---

|  |
| --- |
| ![WARNING](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# HITLayout
<a name="ApiReference_HITLayoutArticle"></a>

**Topics**
+ [Description](#ApiReference_HITLayoutArticle-description)
+ [Obtaining a Layout ID](#ApiReference_HITLayoutArticle-creatingHITlayoutId)
+ [Using a HITLayout](#ApiReference_HITLayoutArticle-usingaHITlayoutId)
+ [Guidelines for Using HITLayouts](#ApiReference_HITLayoutArticle-guidelines-for-using-HITLayout-questions)

## Description
<a name="ApiReference_HITLayoutArticle-description"></a>

A HITLayout is a reusable Amazon Mechanical Turk project template used to provide Human Intelligence Task (HIT) question data for [CreateHIT](ApiReference_CreateHITOperation.md). You can create a HITLayout template by creating a Mechanical Turk project on the [Amazon Mechanical Turk Requester website](https://requester.mturk.com/create/projects/new). For more information about creating a project, see [How to Create a Project](http://docs.aws.amazon.com/AWSMechTurk/latest/RequesterUI/CreatingaHITTemplate.html) in the [Requester UI Guide](http://docs.aws.amazon.com/AWSMechTurk/latest/RequesterUI/).

## Obtaining a Layout ID
<a name="ApiReference_HITLayoutArticle-creatingHITlayoutId"></a>

A **Layout ID** is assigned to each Mechanical Turk project you create on the Requester website. You use the **Layout ID** as the value for `HITLayoutId` when calling `CreateHIT` to identify the HITLayout project template to use. Mechanical Turk projects can contain parameter placeholders in the format `${parameter_name}`. The names for the parameter placeholders used in a HITLayout project template are listed as **Parameters** along with the **Layout ID** on the Requester website.

**To view the Layout ID and the Parameters used in your HITLayout project template**

1.  Go to the [Amazon Mechanical Turk Requester website](https://requester.mturk.com/). Or for the Requester Sandbox site, go to the [Amazon Mechanical Turk Requester Sandbox website](https://requestersandbox.mturk.com/).

1.  Click **Create**, and then click **New Batch with an Existing Project**.

1.  Click the **Project Name** of an existing project to view **Layout ID** and **Parameters**.
![Click Project Name to View LayoutID](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/AWS-Mturk-Existing-Projects-LayoutId-01.jpg)

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
