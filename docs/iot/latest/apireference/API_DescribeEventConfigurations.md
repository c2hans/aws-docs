---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeEventConfigurations.html
---

# DescribeEventConfigurations
<a name="API_DescribeEventConfigurations"></a>

Describes event configurations.

Requires permission to access the [DescribeEventConfigurations](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_DescribeEventConfigurations_RequestSyntax"></a>

```
GET /event-configurations HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeEventConfigurations_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeEventConfigurations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeEventConfigurations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "creationDate": number,
   "eventConfigurations": {
      "string" : {
         "Enabled": boolean
      }
   },
   "lastModifiedDate": number
}
```

## Response Elements
<a name="API_DescribeEventConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationDate](#API_DescribeEventConfigurations_ResponseSyntax) **   <a name="iot-DescribeEventConfigurations-response-creationDate"></a>
The creation date of the event configuration.
Type: Timestamp

 ** [eventConfigurations](#API_DescribeEventConfigurations_ResponseSyntax) **   <a name="iot-DescribeEventConfigurations-response-eventConfigurations"></a>
The event configurations.
Type: String to [Configuration](API_Configuration.md) object map
Valid Keys: `THING | THING_GROUP | THING_TYPE | THING_GROUP_MEMBERSHIP | THING_GROUP_HIERARCHY | THING_TYPE_ASSOCIATION | JOB | JOB_EXECUTION | POLICY | CERTIFICATE | CA_CERTIFICATE`

 ** [lastModifiedDate](#API_DescribeEventConfigurations_ResponseSyntax) **   <a name="iot-DescribeEventConfigurations-response-lastModifiedDate"></a>
The date the event configurations were last modified.
Type: Timestamp

## Errors
<a name="API_DescribeEventConfigurations_Errors"></a>

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

## See Also
<a name="API_DescribeEventConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/DescribeEventConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/DescribeEventConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DescribeEventConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/DescribeEventConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DescribeEventConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/DescribeEventConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/DescribeEventConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/DescribeEventConfigurations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/DescribeEventConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DescribeEventConfigurations)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
