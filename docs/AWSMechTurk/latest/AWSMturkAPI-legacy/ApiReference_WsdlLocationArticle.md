---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_WsdlLocationArticle.html
---

**Amazon Mechanical Turk will permanently close on September 30, 2026.** For Workers and Requesters currently using the service, visit our [Amazon Mechanical Turk help page](https://www.mturk.com/help) to learn how you can prepare for this closure.

|  |
| --- |
| ![WARNING](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# WSDL and Schema Locations
<a name="ApiReference_WsdlLocationArticle"></a>

**Topics**
+ [API Release Notes](#api-release-notes)
+ [The WSDL and Message Schema Locations](#the-wsdl-and-message-schema-locations)
+ [The Data Structure Schema Locations](#the-data-structure-schema-locations)
+ [The Formatted Content XHTML Subset](#the-formatted-content-xhtml-subset)
+ [The Notification API WSDL Location](#the-notifications-receptor-wsdl-location)
+ [Service API Versions](#service-api-versions)
+ [Accessing a Specific Service Version](#accessing-a-specific-service-version)
+ [The Default Version](#the-default-version)

 The Amazon Mechanical Turk Service can be accessed using the SOAP web services messaging protocol, or using the REST method of HTTP requests with parameters. The SOAP interface is described by a Web Services Description Language (WSDL) document. REST requests return messages that conform to an XML Schema document.

 To make it easy to upgrade your application when a new version of schemas are released, all schemas have a version number. The version number appears in the URL of a schema file, and in a schema's target namespace. The API schemas (the WSDL and request/response messages) and the data structure schemas (question and answer values) use separate version numbers. The latest versions are as follows:

|  Type of Schema  |  Latest Version  |
| --- | --- |
|  The API: WSDL and message schemas  |  2014-08-15  |
|  The HTMLQuestion schema  |  2011-11-11  |
|  The QuestionForm, QuestionFormAnswers and AnswerKey schemas  |  2005-10-01  |
|  The ExternalQuestion schema  |  2006-07-14  |
|  The formatted content XHTML subset  |  2006-07-14  |
|  The Notification API  |  2006-05-05  |

## API Release Notes
<a name="api-release-notes"></a>

 See the [API release notes](http://aws.amazon.com/releasenotes/Amazon-Mechanical-Turk) for new features and bug fixes.

## The WSDL and Message Schema Locations
<a name="the-wsdl-and-message-schema-locations"></a>

 The WSDL for a given version of the Amazon Mechanical Turk Service API can be found at a URL that corresponds to the API version. For example, the WSDL for the **2014-08-15** version of the API can be found here:

 [http://mechanicalturk.amazonaws.com/AWSMechanicalTurk/2014-08-15/AWSMechanicalTurkRequester.wsdl](http://mechanicalturk.amazonaws.com/AWSMechanicalTurk/2014-08-15/AWSMechanicalTurkRequester.wsdl)

 The XML Schema for the messages of a given version of the Amazon Mechanical Turk Service API can be found at a URL that corresponds to the API version. For example, the XML Schema for the **2014-08-15** version of the API can be found here:

 [http://mechanicalturk.amazonaws.com/AWSMechanicalTurk/2014-08-15/AWSMechanicalTurkRequester.xsd](http://mechanicalturk.amazonaws.com/AWSMechanicalTurk/2014-08-15/AWSMechanicalTurkRequester.xsd)

## The Data Structure Schema Locations
<a name="the-data-structure-schema-locations"></a>

 The Amazon Mechanical Turk Service has several parameters and return values that contain XML data. The XML content must validate against the appropriate XML schema. For more information, see [HTMLQuestion](ApiReference_HTMLQuestionArticle.md), [QuestionForm](ApiReference_QuestionFormDataStructureArticle.md), [QuestionFormAnswers](ApiReference_QuestionFormAnswersDataStructureArticle.md), and [AnswerKey](ApiReference_AnswerKeyDataStructureArticle.md).

**Note**
 The API version number and the data structure version number are not related. The two sets of schemas may have new releases at different times, and may have different version numbers. For example, an application using the **2014-08-15** version of the API may create HITs using the **2005-10-01** version of the QuestionForm schema. (There may not be a "2014-08-15" version of the QuestionForm schema.)
 Your application may use any supported version of the data schemas with any supported version of the API. A data structure returned by the service will include a namespace that corresponds to the relevant schema.

 The **2011-11-11** version of the HTMLQuestion schema can be found here:

 [http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2011-11-11/HTMLQuestion.xsd](http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2011-11-11/HTMLQuestion.xsd)

 The **2005-10-01** version of the QuestionForm schema can be found here:

 [http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2005-10-01/QuestionForm.xsd](http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2005-10-01/QuestionForm.xsd)

 The **2005-10-01** version of the QuestionFormAnswers schema can be found here:

 [http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2005-10-01/QuestionFormAnswers.xsd](http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2005-10-01/QuestionFormAnswers.xsd)

 The **2005-10-01** version of the AnswerKey schema can be found here:

 [http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2005-10-01/AnswerKey.xsd](http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2005-10-01/AnswerKey.xsd)

 The **2006-07-14** version of the ExternalQuestion schema can be found here:

 [http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2006-07-14/ExternalQuestion.xsd](http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2006-07-14/ExternalQuestion.xsd)

**Note**
 To conform to a schema, XML content must use namespace declarations that match the target namespace for the schema. The target namespace is declared at the top of the schema, as the "targetNamespace" attribute of the "xs:schema" element.
 The schemas for QuestionForm, QuestionFormAnswers, and AnswerKey use namespace URIs similar to the URL at which the schema file can be found, including the service version. For example:

```
<QuestionForm
  xmlns="http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2005-10-01/QuestionForm.xsd"
  >
    {{[...]}}
</QuestionForm>
```
 If the service returns an error message about data not validating against the schema, make sure your namespace declaration matches the target namespace specified in the schema.

## The Formatted Content XHTML Subset
<a name="the-formatted-content-xhtml-subset"></a>

 HITs and Qualification tests can include blocks of content formatted with XHTML tags in their instructions and question data. To include text and markup for formatted content in a web service request, you specify it as XML CDATA inside a `FormattedContent` element, part of [the QuestionForm data structure](ApiReference_QuestionFormDataStructureArticle.md).

 Amazon Mechanical Turk validates formatted content by converting the text and markup in the CDATA block into an XML document, then validating it against a schema. For more information about how this XML document is produced, see [Formatted Content: XHTML](ApiReference_FormattedContentXHTMLArticle.md), "How XHTML Formatted Content Is Validated".

 The **2006-07-14** version of the schema used to validate formatted content can be found here:

 [http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2006-07-14/FormattedContentXHTMLSubset.xsd](http://mechanicalturk.amazonaws.com/AWSMechanicalTurkDataSchemas/2006-07-14/FormattedContentXHTMLSubset.xsd)

## The Notification API WSDL Location
<a name="the-notifications-receptor-wsdl-location"></a>

 The WSDL for the Notification API is located at:

 [http://mechanicalturk.amazonaws.com/AWSMechanicalTurk/2006-05-05/AWSMechanicalTurkRequesterNotification.wsdl](http://mechanicalturk.amazonaws.com/AWSMechanicalTurk/2006-05-05/AWSMechanicalTurkRequesterNotification.wsdl)

 For more information about the Notification API, see [The Notification API](ApiReference_NotificationReceptorAPIArticle.md).

## Service API Versions
<a name="service-api-versions"></a>

 When a new version of the service API is released, previous versions are supported for a limited time to allow applications to continue to function until they are upgraded. The version of a service API is specified as a date, such as **2014-08-15**.

 The version of the API can be found in the URLs of the WSDL and schema files. It can also be found in the `targetNamespace` of the WSDL and schema files.

 You can retrieve the WSDL or schema files for previous versions of the API by replacing the version date in the URL with the desired version. For example, to retrieve the WSDL for API version **2014-08-15**:

 [http://mechanicalturk.amazonaws.com/AWSMechanicalTurk/2014-08-15/AWSMechanicalTurkRequester.wsdl](http://mechanicalturk.amazonaws.com/AWSMechanicalTurk/2014-08-15/AWSMechanicalTurkRequester.wsdl)

## Accessing a Specific Service Version
<a name="accessing-a-specific-service-version"></a>

 For your application to use a specific version of the service API, the service needs to be told which version is being used with each request.

 For SOAP requests, the Amazon Mechanical Turk Service determines which API version you are using based on the namespace in your request message, which is determined by the WSDL you are using with your application. SOAP requests always include this information, and SOAP toolkits determine the namespace automatically from the WSDL.

 For REST requests, you must explicitly request the version to use by including the `Version` parameter in your request. The `Version` parameter ensures that the service does not return response elements that your application is not designed to handle.

 Here is an example REST request that includes the `Version` parameter:

```
https://mechanicalturk.amazonaws.com/?Service=AWSMechanicalTurkRequester
&AWSAccessKeyId={{[the Requester's Access Key ID]}}
&Version=2014-08-15
&Operation=GetHIT
&HITId=123RVWYBAZW00EXAMPLE
```

## The Default Version
<a name="the-default-version"></a>

 Older AWS services supported requests that did not specify an API version. This behavior is still supported for legacy reasons, but its use is discouraged.

 When the Amazon Mechanical Turk Service receives a REST request without a `Version` parameter, the service will use the latest version. If your application does not specify the `Version` in each request, when a new version of the API is released, your application will start using the new version automatically. Because new versions of the API may be incompatible with applications expecting to use an older version, specifying an explicit `Version` parameter with each request is strongly recommended.

 A similar legacy feature exists for SOAP: A request for the WSDL or a schema file using a URL that does not include the version number will return the file for the latest version of the API. Using WSDL/schema URLs that include the API version number is strongly recommended.
