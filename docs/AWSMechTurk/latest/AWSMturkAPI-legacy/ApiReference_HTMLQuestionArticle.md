---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_HTMLQuestionArticle.html
---

|  |
| --- |
| ![WARNING](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# HTMLQuestion
<a name="ApiReference_HTMLQuestionArticle"></a>

**Topics**
+ [Description](#ApiReference_HTMLQuestionArticle-description)
+ [The HTMLQuestion Data Structure](#ApiReference_HTMLQuestionArticle-the-HTMLQuestion-data-structure)
+ [Example](#ApiReference_HTMLQuestionArticle-example)
+ [Preview Mode](#ApiReference_HTMLQuestionArticle-the-external-form-preview-mode)
+ [The Form Action](#ApiReference_HTMLQuestionArticle-the-external-form-the-form-action)
+ [The Answer Data](#ApiReference_HTMLQuestionArticle-the-answer-data)
+ [Guidelines For Using HTML Questions](#ApiReference_HTMLQuestionArticle-guidelines-for-using-external-questions)

## Description
<a name="ApiReference_HTMLQuestionArticle-description"></a>

 The `HTMLQuestion` data structure defines one or more questions for a HIT using HTML. The `HTMLQuestion` data structure is similar to both the `QuestionForm` and `ExternalQuestion` data structures.

The `QuestionForm` data structure defines, using a special XML language, how Amazon Mechanical Turk displays HIT questions and collects the answers. The `ExternalQuestion` data structure defines, using HTML, questions you host on your own "external" website. If you want to define your questions using HTML forms without having to host a website, you can use the `HTMLQuestion` data structure.

A `HTMLQuestion` HIT is like a cross between a `QuestionForm` HIT and an `ExternalQuestion` HIT, for instance:
+ Like a `QuestionForm` HIT, you do not need to run a website or run any other infrastructure to have your HIT display on Mechanical Turk. You define your question when you call CreateHIT and then collect worker answers later, after they have been submitted.
+  Like an `ExternalQuestion` HIT, you can define your HIT in HTML. Your HTML code must contain a form for the Worker to fill out and submit, which is displayed in a frame in the Worker's web browser. The Worker submits results using your form, and your form submits the results back to Amazon Mechanical Turk. Worker answers are processed by Mechanical Turk in the same way as `ExternalQuestion` HITs. If you choose, you can collect or process the results before submitting to Mechanical Turk.

The worker interaction and presentation options available for `HTMLQuestion` are similar to `ExternalQuestion`. HTMLQuestions differ from ExternalQuestions primarily in how they are created.

As with the other question data structures, an `HTMLQuestion` is a string value that consists of XML data. This data must conform to the `HTMLQuestion` schema. See [WSDL and Schema Locations](ApiReference_WsdlLocationArticle.md) for the location of this schema. For more information about using XML data as a parameter or return value, see [Using XML Parameter Values](ApiReference_XMLParameterValuesArticle.md).

**Note**
You can only use an `HTMLQuestion` as the question of a HIT. You cannot use an `HTMLQuestion` with a Qualification test.

The `HTMLQuestion` data structure is used as a parameter value for the following operation:
+  `CreateHIT`

The `HTMLQuestion` data structure is a value in a [HIT](ApiReference_HITDataStructureArticle.md) data structure.

All elements in an `HTMLQuestion` belong to a namespace whose name is identical to the URL of the `HTMLQuestion` schema document for the version of the API you are using.

## The HTMLQuestion Data Structure
<a name="ApiReference_HTMLQuestionArticle-the-HTMLQuestion-data-structure"></a>

 The `HTMLQuestion` data structure has a root element of `HTMLQuestion`.

 The `HTMLQuestion` element contains the following elements:

| Name | Description | Required |
| --- | --- | --- |
|  `HTMLContent`  | The HTML code of your web form, to be displayed in a frame in the Worker's web browser. The HTML must validate against the HTML5 specification. HTML5 is backwards-compatible with a variety of recent HTML document specifications. For more information, see [http://www.w3.org/TR/html5-diff/](http://www.w3.org/TR/html5-diff/). For help in ensuring that your HTML validates, see [http://validator.w3.org](http://validator.w3.org).<br />Type: String<br />Default: None<br />Amazon Mechanical Turk appends the following parameters to this URL: `assignmentId`, `hitId`, `turkSubmitTo`, and `workerId`. For more information about these appended parameters, see the sections following this table. | Yes |
|  `FrameHeight`  | The height of the frame, in pixels.<br />Type: Integer<br />Default: None | Yes |

## Example
<a name="ApiReference_HTMLQuestionArticle-example"></a>

The following is an example of a complete `HTMLQuestion` data structure. Remember that to pass this structure in as the value of a parameter to an operation, XML characters must be escaped as character entities. For more information, see [Using XML Parameter Values](ApiReference_XMLParameterValuesArticle.md).

```
<HTMLQuestion xmlns="[the HTMLQuestion schema URL]">
  <HTMLContent><![CDATA[
<!DOCTYPE html>
<html>
 <head>
  <meta http-equiv='Content-Type' content='text/html; charset=UTF-8'/>
  <script type='text/javascript' src='https://s3.amazonaws.com/mturk-public/externalHIT_v1.js'></script>
 </head>
 <body>
  <form name='mturk_form' method='post' id='mturk_form' action='https://www.mturk.com/mturk/externalSubmit'>
  <input type='hidden' value='' name='assignmentId' id='assignmentId'/>
  <h1>What's up?</h1>
  <p><textarea name='comment' cols='80' rows='3'></textarea></p>
  <p><input type='submit' id='submitButton' value='Submit' /></p></form>
  <script language='Javascript'>turkSetAssignmentID();</script>
 </body>
</html>
]]>
  </HTMLContent>
  <FrameHeight>450</FrameHeight>
</HTMLQuestion>
```

## Preview Mode
<a name="ApiReference_HTMLQuestionArticle-the-external-form-preview-mode"></a>

The question defined by `HTMLQuestion` displays when a Worker previews the HIT on the Amazon Mechanical Turk website, before the Worker clicks the **Accept HIT** button. When the HIT is being previewed, the URL has a special value for the `assignmentId`: `ASSIGNMENT_ID_NOT_AVAILABLE`. This is the same mechanism used for `ExternalQuestion` HITs.

When a Worker previews a HIT, your HTML should show the Worker everything they will need to do to complete the HIT, so they can decide whether or not to accept it. The easiest way to do this is to simply display the form as it would appear when the HIT is accepted. However, you may want to take precautions to prevent a Worker from accidentally filling out or submitting your form prior to accepting the HIT.

You can use JavaScript to check the `assignmentId` parameter, and change the display of the form if the HIT is being previewed (`assignmentId=ASSIGNMENT_ID_NOT_AVAILABLE`).

## The Form Action
<a name="ApiReference_HTMLQuestionArticle-the-external-form-the-form-action"></a>

For information about form actions for `HTMLQuestion`, see " The Form Action" in [ExternalQuestion](ApiReference_ExternalQuestionArticle.md).

## The Answer Data
<a name="ApiReference_HTMLQuestionArticle-the-answer-data"></a>

For information about answer data for `HTMLQuestion`, see " The Answer Data" in [ExternalQuestion](ApiReference_ExternalQuestionArticle.md).

## Guidelines For Using HTML Questions
<a name="ApiReference_HTMLQuestionArticle-guidelines-for-using-external-questions"></a>

**Tip**
Your HTML code can do many things inside the browser frame, but eventually it must cause the Worker's browser to load the "externalSubmit" URL in the frame with the results in POST data. The easiest way to do this is with an HTML form whose fields contain the HIT results, with a submit button that the Worker clicks. If a `HTMLQuestion` HIT prevents the Worker from submitting results back to Amazon Mechanical Turk using the "externalSubmit" mechanism, the Worker may not be able to claim rewards or continue doing work without restarting their session. Amazon Mechanical Turk reserves the right to remove any `HTMLQuestion` HITs that are not functioning properly.

**Note**
Your HIT will be rendered inside an IFRAME that has certain limitations. The IFRAME operates in HTML5 “sandbox” mode that has extra restrictions on the content that can appear in the frame. This limits your ability to execute certain code and to use technologies such as Adobe Flash. To ensure your HITs work as expected, we recommend you test them first in the [Requester Sandbox](https://requester.mturk.com/developer/sandbox).

**Tip**
All `HTMLQuestion` HITs are served from the same domain, regardless of requester. Bear this in mind if you choose to set cookies from JavaScript in your HTML.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Mechanical Turk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSMechTurk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
