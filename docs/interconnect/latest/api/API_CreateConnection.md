---
source_url: https://docs.aws.amazon.com/interconnect/latest/api/API_CreateConnection.html
---

# CreateConnection
<a name="API_CreateConnection"></a>

Initiates the process to create a Connection across the specified Environment.

The Environment dictates the specified partner and location to which the other end of the connection should attach. You can see a list of the available Environments by calling [ListEnvironments](API_ListEnvironments.md)

The [AttachPoint](API_AttachPoint.md) specifies where within the AWS Network your connection will logically connect.

After a successful call to this method, the resulting [Connection](API_Connection.md) will return an Activation Key which will need to be brought to the specific partner's portal to confirm the [Connection](API_Connection.md) on both sides. (See [Environment:activationPageUrl](API_Environment.md#interconnect-Type-Environment-activationPageUrl) for a direct link to the partner portal).

## Request Parameters
<a name="API_CreateConnection_RequestParameters"></a>

 ** attachPoint **
The [AttachPoint](API_AttachPoint.md) to which the connection should be associated."
Type: [AttachPoint](API_AttachPoint.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** bandwidth **
The desired bandwidth of the requested [Connection](API_Connection.md)
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8.
Pattern: `\d+[MG]bps`
Required: Yes

 ** clientToken **
Idempotency token used for the request.
Type: String
Required: No

 ** description **
A description to distinguish this [Connection](API_Connection.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[-a-zA-Z0-9_ ]+`
Required: No

 ** environmentId **
The identifier of the [Environment](API_Environment.md) across which this [Connection](API_Connection.md) should be created.
The available [Environment](API_Environment.md) objects can be determined using [ListEnvironments](API_ListEnvironments.md).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** remoteAccount **
Account and/or principal identifying information that can be verified by the partner of this specific Environment.
Type: [RemoteAccountIdentifier](API_RemoteAccountIdentifier.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** tags **
The tag to associate with the resulting [Connection](API_Connection.md).
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Elements
<a name="API_CreateConnection_ResponseElements"></a>

The following element is returned by the service.

 ** connection **
The resulting [Connection](API_Connection.md).
Type: [Connection](API_Connection.md) object

## Errors
<a name="API_CreateConnection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The calling principal is not allowed to access the specified resource, or the resource does not exist.
HTTP Status Code: 403

 ** InterconnectClientException **
The request was denied due to incorrect client supplied parameters.
HTTP Status Code: 400

 ** InterconnectServerException **
The request resulted in an exception internal to the service.
HTTP Status Code: 500

 ** InterconnectValidationException **
The input fails to satisfy the constraints specified.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The request specifies a resource that does not exist on the server.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The requested operation would result in the calling principal exceeding their allotted quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

## See Also
<a name="API_CreateConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/interconnect-2022-07-26/CreateConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/interconnect-2022-07-26/CreateConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/interconnect-2022-07-26/CreateConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/interconnect-2022-07-26/CreateConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/interconnect-2022-07-26/CreateConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/interconnect-2022-07-26/CreateConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/interconnect-2022-07-26/CreateConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/interconnect-2022-07-26/CreateConnection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/interconnect-2022-07-26/CreateConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/interconnect-2022-07-26/CreateConnection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Interconnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query interconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
