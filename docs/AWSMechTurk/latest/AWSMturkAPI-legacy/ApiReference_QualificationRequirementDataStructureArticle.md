---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/ApiReference_QualificationRequirementDataStructureArticle.html
---

**Amazon Mechanical Turk will permanently close on September 30, 2026.** For Workers and Requesters currently using the service, visit our [Amazon Mechanical Turk help page](https://www.mturk.com/help) to learn how you can prepare for this closure.

|  |
| --- |
| ![WARNING](https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/images/warn.png)<br /> You are browsing the documentation for a deprecated version ('2014-08-15') of the Amazon Mechanical Turk Requester API. **This version of the API will be deprecated and will be rendered unusable as of June 1st, 2019.**<br />If you request against a legacy API version (https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI-legacy/Welcome.html) on or after June 1, 2019, you will receive the following response:<br />`This Requester API is no longer supported. Please use the latest API using the official AWS SDK. https://aws.amazon.com/getting-started/tools-sdks` <br /> The latest version of our API ('2017-01-17') provides you with additional tool choices and enables you to select from nine [AWS Software Development Kits](https://aws.amazon.com/tools/) (SDKs) that have been widely adopted across the AWS community. This API can be accessed using the following AWS SDKs: [Python/Boto](https://aws.amazon.com/sdk-for-python/) (Boto3), Javascript ([NodeJS](https://aws.amazon.com/sdk-for-node-js/) or [Browser](https://aws.amazon.com/sdk-for-browser/)), [Java](https://aws.amazon.com/sdk-for-java/), [.NET](https://aws.amazon.com/sdk-for-net/), [Go](https://aws.amazon.com/sdk-for-go/), [Ruby](https://aws.amazon.com/sdk-for-ruby/), [PHP](https://aws.amazon.com/sdk-for-php/) or [C\+\+](https://aws.amazon.com/sdk-for-cpp/). This version also makes it easier for customers to connect MTurk with other AWS services like [S3](https://aws.amazon.com/s3/), [Lambda](https://aws.amazon.com/lambda/), [Step Functions](https://aws.amazon.com/step-functions/), [Lex](https://aws.amazon.com/lex/), [Polly](https://aws.amazon.com/polly/), [Rekognition](https://aws.amazon.com/rekognition/), [Amazon SageMaker](https://aws.amazon.com/sagemaker/), [AWS Batch](https://aws.amazon.com/batch/), [EC2](https://aws.amazon.com/ec2/), and more. <br /> This version also updates naming conventions used in the API and adopts the AWS standard of [Signature Version 4](http://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) to authenticate requests securely. The API uses REST requests and no longer requires that developers be familiar with SOAP protocol. These changes make the MTurk API consistent with AWS APIs, simplifying the on-boarding process for both new and existing AWS developers. The legacy MTurk Command Line Tools and .NET, Java, Ruby, and Perl SDKs were marked as deprecated in January 2018. We will be deprecating the legacy APIs as of June 1, 2019. <br /> If you are on a legacy API, you must migrate to the [latest version](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) of our API. You can find documentation for the latest API [here](http://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/Welcome.html) and the AWS SDKs [here](https://aws.amazon.com/getting-started/tools-sdks/). Please check whether you need to migrate and review the [technical migration guide](https://medium.com/@mechanicalturk/mturk-requester-api-migration-guide-3497398ba37f). <br />For support, contact [requestor-apilegacydeprecation-support@amazon.com](mailto:requestor-apilegacydeprecation-support@amazon.com). |

# QualificationRequirement
<a name="ApiReference_QualificationRequirementDataStructureArticle"></a>

**Topics**
+ [Description](#ApiReference_QualificationRequirementDataStructureArticle-description)
+ [Using Custom, System-Assigned, and Master Qualification Types](#CustomQualificationsandSystemQualifications)
+ [Elements](#ApiReference_QualificationRequirementDataStructureArticle-elements)
+ [Qualification Type IDs](#ApiReference_QualificationType-IDs)
+ [Master Qualifications](#MasterQualifications)
+ [Adding Adult Content](#AdultContent)
+ [The Locale Qualification](#ApiReference_QualificationRequirementDataStructureArticle-the-locale-qualification)
+ [Example—Using the QualificationRequirement Data Structure](#ApiReference_QualificationRequirementDataStructureArticle-sample1-createhit)
+ [Example—Using the QualificationRequirement Data Structure for Comparing Multiple Values](#ApiReference_QualificationRequirementDataStructureArticle-sample-createhit)

## Description
<a name="ApiReference_QualificationRequirementDataStructureArticle-description"></a>

 The QualificationRequirement data structure describes a Qualification a Worker must have before the Worker is allowed to accept a HIT. A requirement may optionally state that a Worker must have the Qualification to preview the HIT.

 The QualificationRequirement data structure is used as a parameter for the following operations:
+  `CreateHIT`
+  `RegisterHITType`

 The QualificationRequirement data structure is used in the [HIT data structure](ApiReference_HITDataStructureArticle.md).

## Using Custom, System-Assigned, and Master Qualification Types
<a name="CustomQualificationsandSystemQualifications"></a>

A Qualification requirement can be based on a Qualification you assign to Workers. You can create a custom Qualification type using the `CreateQualificationType` operation. Then you can grant requests for the Qualification automatically using a Qualification test and answer key submitted with the Qualification type, or you can grant the request manually with the `GrantQualification` operation. The `CreateQualificationType` returns a `QualificationTypeId`, which you can use with the `QualificationRequirement` data structure to identify the type of Qualification the Worker is required to have to accept a HIT. Either the Qualification test or your call to `GrantQualification` determines a Qualification value, which is compared to the requirement in the HIT to determine the Worker's eligibility.

Amazon Mechanical Turk supplies several Qualification types for use by all Requesters. Mechanical Turk system-assigned Qualification types work the same way as Qualifications that you create, except that data from the Mechanical Turk marketplace determines the Worker’s values. Every Worker has a value for each system Qualification, and these values are updated as the Worker uses the system. Additionally, Amazon Mechanical Turk also provides Master Qualification types that give you access to an elite group of Workers who have demonstrated superior performance while completing thousands of HITs across the Mechanical Turk marketplace. You can use the Master and system-assigned Qualification types by using the corresponding Qualification type ID in the `QualificationTypeId` element of the `QualificationRequirement` data structure. For a list of the Master and system-assigned IDs, see [Qualification Type IDs](#ApiReference_QualificationType-IDs). For more information about using a Master Qualification type, see [Master Qualifications](#MasterQualifications).

## Elements
<a name="ApiReference_QualificationRequirementDataStructureArticle-elements"></a>

 The QualificationRequirement data structure can contain the following elements.

| Name | Description | Value |
| --- | --- | --- |
|  QualificationTypeId  |  The ID of the Qualification type for the requirement.  |  A valid QualificationType ID from a custom Qualification type you created or an ID from the list of Master and system-assigned [Qualification Type IDs](#ApiReference_QualificationType-IDs). |
|  Comparator  |  The kind of comparison to make against a Qualification's value. <br /> You can compare a Qualification's value:+  To an `IntegerValue` to see if it is `LessThan`, `LessThanOrEqualTo`, `GreaterThan`, `GreaterThanOrEqualTo`, `EqualTo`, or `NotEqualTo` the `IntegerValue`.  <br />+  To a `LocaleValue` to see if it is `EqualTo`, or `NotEqualTo` the `LocaleValue`. <br />+  To see if the value is `In` or `NotIn` a set of `IntegerValue` or `LocaleValue` values. <br /> A Qualification requirement can also test if a Qualification `Exists` or `DoesNotExist` in the user's profile, regardless of its value.  |  `LessThan` \| `LessThanOrEqualTo` \| `GreaterThan` \| `GreaterThanOrEqualTo` \| `EqualTo` \| `NotEqualTo` \| `Exists` \| `DoesNotExist` \| `In` \| `NotIn`  |
|  IntegerValue  | The integer value to compare against the Qualification's value. <br /> `IntegerValue` must not be present if `Comparator` is `Exists` or `DoesNotExist`. <br /> `IntegerValue` can only be used if the Qualification type has an integer value; it cannot be used with the `Worker_Locale` QualificationType ID, see [Qualification Type IDs](#ApiReference_QualificationType-IDs).<br /> When performing a set comparison by using the `In` or the `NotIn` comparator, you can use up to 15 `IntegerValue` elements in a QualificationRequirement data structure. For an example of a set comparison, see [Example—Using the QualificationRequirement Data Structure for Comparing Multiple Values](#ApiReference_QualificationRequirementDataStructureArticle-sample-createhit). | An integer.  |
|  LocaleValue  |  The locale value to compare against the Qualification's value. The local value must be a valid [ ISO 3166 country code](http://www.iso.org/iso/country_codes/iso_3166_code_lists.htm) or supports [ISO 3166-2 subdivisions](http://en.wikipedia.org/wiki/ISO_3166-2:US). <br /> `LocaleValue` can only be used with a `Worker_Locale` QualificationType ID, see [Qualification Type IDs](#ApiReference_QualificationType-IDs). <br /> `LocaleValue` can only be used with the `EqualTo`, `NotEqualTo`, `In`, and `NotIn` comparators. <br /> You must only use a single `LocaleValue` element when using the `EqualTo` or `NotEqualTo` comparators. <br /> When performing a set comparison by using the `In` or the `NotIn` comparator, you can use up to 30 `LocaleValue` elements in a QualificationRequirement data structure. For an example of a set comparison, see [Example—Using the QualificationRequirement Data Structure for Comparing Multiple Values](#ApiReference_QualificationRequirementDataStructureArticle-sample-createhit). | A [Locale](ApiReference_LocaleDataStructureArticle.md) data structure. |
|  RequiredToPreview  |  If **true**, the question data for the HIT will not be shown when a Worker whose Qualifications do not meet this requirement tries to preview the HIT. That is, a Worker's Qualifications must meet all of the requirements for which `RequiredToPreview` is **true** in order to preview the HIT. <br /> If a Worker meets all of the requirements where `RequiredToPreview` is **true** (or if there are no such requirements), but does not meet all of the requirements for the HIT, the Worker will be allowed to preview the HIT's question data, but will not be allowed to accept and complete the HIT. <br /> The default is **false**.  |  A Boolean value, **true** or **false**  |

## Qualification Type IDs
<a name="ApiReference_QualificationType-IDs"></a>

 The following table lists the Master and system-assigned Qualification Type IDs that can be used in the `QualificationTypeId` element.

|  Name  |  QualificationTypeId  |  Description  |
| --- | --- | --- |
| Masters | Sandbox: 2ARFPLSP75KLA8M8DH1HTEQVJT3SY6<br />Production: 2F1QJWKUDD8XADTFD2Q0G6UTO95ALH | Masters are an elite group of Workers, who have demonstrated superior performance while completing thousands of HITs across the Mechanical Turk marketplace. Masters must maintain this high level of performance or they may lose this distinction. Set the `comparator` parameter to "Exists" to require that Workers have this Qualification. <br />Note that for this Qualification type ID, the `QualificationTypeId` value for the Mechanical Turk Sandbox environment is different than the value for the production environment. |
| Worker\_​NumberHITsApproved |  00000000000000000040  | Specifies the total number of HITs submitted by a Worker that have been approved. The value is an integer greater than or equal to 0.  |
| Worker\_Locale  |  00000000000000000071  | The location of the Worker, as specified in the Worker's mailing address. For more information about the locale Qualification, see the [The Locale Qualification](#ApiReference_QualificationRequirementDataStructureArticle-the-locale-qualification) section.  |
| Worker\_Adult |  00000000000000000060  | Requires workers to acknowledge that they are over 18 and that they agree to work on potentially offensive content. The value type is boolean, 1 (required), 0 (not required, the default). |
|  Worker\_​PercentAssignmentsApproved  |  000000000000000000L0  | The percentage of assignments the Worker has submitted that were subsequently approved by the Requester, over all assignments the Worker has submitted. The value is an integer between 0 and 100. <br />Note that a Worker's approval rate is statistically meaningless for small numbers of assignments, since a single rejection can reduce the approval rate by many percentage points. So to ensure that a new Worker's approval rate is unaffected by these statistically meaningless changes, if a Worker has submitted less than 100 assignments, the Worker's approval rate in the system is 100%.<br />To prevent Workers who have less than 100 approved assignments from working on your HIT, set the Worker\_​NumberHITsApproved qualification type ID to a value greater than 100. |

## Master Qualifications
<a name="MasterQualifications"></a>

You can require that Workers must have a Master Qualification to complete your HITs.

To create a Qualification requirement for Masters, specify:
+  A `QualificationTypeId` of 2F1QJWKUDD8XADTFD2Q0G6UTO95ALH
+  A `Comparator` of `Exists`

**Note**
 The Master Qualification Type ID values used for the `QualificationTypeId` parameter in the preceding procedures are for the production environment. The ID values to use in the Mechanical Turk Sandbox environment are listed in the [Qualification Type IDs](#ApiReference_QualificationType-IDs) table.

## Adding Adult Content
<a name="AdultContent"></a>

Adult content can be offensive to some people. For that reason, if your HIT is adult-oriented, we ask you to use the following procedure.

**Adding Adult HITs**

1. In the HIT title, include the words "adult content."

1. Specify the worker's qualifications in one of the following ways:

<table>
<tbody>
  <tr><td>Using the API:<ul><li> Set the <code>CreateHit</code> parameter, <code>QualificationRequirement</code>, to the qualification type, 00000000000000000060. </li><li> Set <code>comparator</code> parameter to "EqualTo."  </li><li>  Set the <code>IntegerValue</code> parameter to 1 (required). </li></ul></td></tr>
  <tr><td>Using the command line tools, in the HIT properties file:<ul><li> Set <code>qualificationTypeId</code> to 00000000000000000060. </li><li> Set <code>comparator</code>, to "EqualTo."  </li><li>  Set the <code>IntegerValue</code> to 1 (required). For example, <pre><QualificationRequirement><br />  <QualificationTypeId>00000000000000000060</QualificationTypeId><br />  <Comparator>EqualTo</Comparator><br />  <IntegerValue>1</IntegerValue><br /></QualificationRequirement></pre> </li></ul></td></tr>
</tbody>
</table>

1. Define the HIT to be private or previewed.

   This setting prevents anyone who does not qualify from seeing the HIT. To make the HIT private, use one of the following methods:

<table>
<tbody>
  <tr><td>Using the API, set the <code>RequiredToPreview</code> parameter to true.</td></tr>
  <tr><td>Using the command line tools, in the HIT properties file, set the private parameter, <code>qualification.private</code>, to TRUE. </td></tr>
</tbody>
</table>

## The Locale Qualification
<a name="ApiReference_QualificationRequirementDataStructureArticle-the-locale-qualification"></a>

 You can create a Qualification requirement based on the Worker's location. The Worker's location is specified by the Worker to Amazon Mechanical Turk when the Worker creates his account.

 To create a Qualification requirement based on the Worker's location, specify:
+  A `QualificationTypeId` of 00000000000000000071
+  A `Comparator` of `EqualTo` or `NotEqualTo`
+  A `LocaleValue` that corresponds to the desired locale

 To create a Qualification requirement based on the Worker being in or not in one of several locations, specify:
+  A `QualificationTypeId` of 00000000000000000071
+  A `Comparator` of `In` or `NotIn`
+  Multiple `LocaleValue` values that correspond to the desired locales.

 For more information on the format of a `LocaleValue` element, see [Locale data structure](ApiReference_LocaleDataStructureArticle.md).

### Example
<a name="ApiReference_QualificationRequirementDataStructureArticle-the-locale-qualification-example"></a>

 The following example shows a QualificationRequirement specifying Workers located in the state of Pennsylvania. Workers located in the state of New York (US-NY) or in the country of India (IN) do not qualify for the HITs with this QualificationRequirement.

```
<QualificationRequirement>
  <QualificationTypeId>00000000000000000071</QualificationTypeId>
  <Comparator>EqualTo</Comparator>
  <LocaleValue>
  <Country>US</Country>
  <Subdivision>PA</Subdivision>
  </LocaleValue>
  </QualificationRequirement>
```

 The following example shows a QualificationRequirement specifying Workers not located in the state of California. Workers located in the state of New York or in the country of India (IN) will be qualified to do HITs with this QualificationRequirement.

```
<QualificationRequirement>
  <QualificationTypeId>00000000000000000071</QualificationTypeId>
  <Comparator>NotEqualTo</Comparator>
  <LocaleValue>
  <Country>US</Country>
  <Subdivision>CA</Subdivision>
  </LocaleValue>
  </QualificationRequirement>
```

## Example—Using the QualificationRequirement Data Structure
<a name="ApiReference_QualificationRequirementDataStructureArticle-sample1-createhit"></a>

 The following example of a QualificationRequirement data structure could be passed in to a call to `CreateHIT`. `CreateHIT` accepts parameters that describe the HIT being created, including one or more Qualification requirements.

### Example SOAP Request
<a name="ApiReference_QualificationRequirementDataStructureArticle-sample1-soap-request"></a>

 In a SOAP request, the QualificationRequirement data structure is specified as the `QualificationRequirement` parameter in XML:

```
<QualificationRequirement>
  <QualificationTypeId>789RVWYBAZW00EXAMPLE</QualificationTypeId>
  <Comparator>GreaterThan</Comparator>
  <IntegerValue>18</IntegerValue>
  </QualificationRequirement>
```

### Example REST Request
<a name="ApiReference_QualificationRequirementDataStructureArticle-sample1-soap-response"></a>

 In a REST request, the components of the QualificationRequirement data structure are specified as separate parameters. To specify more than one `QualificationRequirement` in a REST request, increment the sequence number in the parameter name for each value:

```
https://mechanicalturk.amazonaws.com/?Service=AWSMechanicalTurkRequester
{{[...]}}
&QualificationRequirement.1.QualificationTypeId=789RVWYBAZW00EXAMPLE
&QualificationRequirement.1.Comparator=GreaterThan
&QualificationRequirement.1.IntegerValue=18
&QualificationRequirement.2.QualificationTypeId=ZSPJXD4F1SFZP7YNJWR0
&QualificationRequirement.2.Comparator=EqualTo
&QualificationRequirement.2.IntegerValue=1
```

## Example—Using the QualificationRequirement Data Structure for Comparing Multiple Values
<a name="ApiReference_QualificationRequirementDataStructureArticle-sample-createhit"></a>

 The following example of a QualificationRequirement data structure could be passed in to a call to `CreateHIT`. `CreateHIT` accepts parameters that describe the HIT being created, including one or more Qualification requirements.

### Example SOAP Request
<a name="ApiReference_QualificationRequirementDataStructureArticle-sample-soap-request"></a>

 The following example shows a QualificationRequirement data structure used in a SOAP request that uses multiple `IntegerValue` values when performing a set comparison by using the `In` comparator.

```
<QualificationRequirement>
  <QualificationTypeId>789RVWYBAZW00EXAMPLE</QualificationTypeId>
  <Comparator>In</Comparator>
  <IntegerValue>10</IntegerValue>
  <IntegerValue>20</IntegerValue>
  <IntegerValue>30</IntegerValue>
</QualificationRequirement>
```

### Example SOAP Response
<a name="ApiReference_QualificationRequirementDataStructureArticle-sample-soap-response"></a>

 The following is an example of a SOAP QualificationRequirement data structure in a response to the preceding example request.

```
<QualificationRequirement>
  <QualificationTypeId>789RVWYBAZW00EXAMPLE</QualificationTypeId>
  <Comparator>In</Comparator>
  <IntegerValue>10</IntegerValue>
  <IntegerValue>20</IntegerValue>
  <IntegerValue>30</IntegerValue>
  <RequiredToPreview>0</RequiredToPreview>
</QualificationRequirement>
```

### Example REST Request
<a name="ApiReference_QualificationRequirementDataStructureArticle-sample-rest-response"></a>

 In a REST request, the components of the QualificationRequirement data structure are specified as separate parameters. The following example shows how to perform set comparisons by using the `In` comparator with multiple `IntegerValue` and `LocaleValue` values.

```
https://mechanicalturk.amazonaws.com/?Service=AWSMechanicalTurkRequester
{{[...]}}
&QualificationRequirement.1.QualificationTypeId=789RVWYBAZW00EXAMPLE
&QualificationRequirement.1.Comparator=In
&QualificationRequirement.1.IntegerValue.1=10
&QualificationRequirement.1.IntegerValue.2=20
&QualificationRequirement.1.IntegerValue.3=30
&QualificationRequirement.2.QualificationTypeId=ZSPJXD4F1SFZP7YNJWR0
&QualificationRequirement.2.Comparator=In
&QualificationRequirement.2.LocaleValue.1.Country=US
&QualificationRequirement.2.LocaleValue.2.Country=CA
&QualificationRequirement.2.LocaleValue.3.Country=MX
```
