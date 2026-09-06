---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_ListServiceSpecificCredentials.html
---

# ListServiceSpecificCredentials
<a name="API_ListServiceSpecificCredentials"></a>

Returns information about the service-specific credentials associated with the specified IAM user. If none exists, the operation returns an empty list. The service-specific credentials returned by this operation are used only for authenticating the IAM user to a specific service. For more information about using service-specific credentials to authenticate to an AWS service, refer to the following docs:
+ For service-specific credentials with CodeCommit, refer to [IAM credentials for CodeCommit: Git credentials, SSH keys, and AWS access keys](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_ssh-keys.html) in the *IAM User Guide*.
+ For service-specific credentials with Amazon Keyspaces (for Apache Cassandra), refer to [Use IAM with Amazon Keyspaces (for Apache Cassandra)](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_keyspaces.html) in the *IAM User Guide*.
+ For services that support long-term API keys, refer to [API keys for AWS services](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_api_keys_for_aws_services.html) in the *IAM User Guide*.

## Request Parameters
<a name="API_ListServiceSpecificCredentials_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** AllUsers **
A flag indicating whether to list service specific credentials for all users. This parameter cannot be specified together with UserName. When true, returns all credentials associated with the specified service.
Type: Boolean
Required: No

 ** Marker **
Use this parameter only when paginating results and only after you receive a response indicating that the results are truncated. Set it to the value of the Marker from the response that you received to indicate where the next call should start.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 320.
Pattern: `[\u0020-\u00FF]+`
Required: No

 ** MaxItems **
Use this only when paginating results to indicate the maximum number of items you want in the response. If additional items exist beyond the maximum you specify, the IsTruncated response element is true.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** ServiceName **
Filters the returned results to only those for the specified AWS service. If not specified, then AWS returns service-specific credentials for all services.
Type: String
Required: No

 ** UserName **
The name of the user whose service-specific credentials you want information about. If this value is not specified, then the operation assumes the user whose credentials are used to call the operation.
This parameter allows (through its [regex pattern](http://wikipedia.org/wiki/regex)) a string of characters consisting of upper and lowercase alphanumeric characters with no spaces. You can also include any of the following characters: \_\+=,.@-
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w+=,.@-]+`
Required: No

## Response Elements
<a name="API_ListServiceSpecificCredentials_ResponseElements"></a>

The following elements are returned by the service.

 ** IsTruncated **
A flag that indicates whether there are more items to return. If your results were truncated, you can make a subsequent pagination request using the Marker request parameter to retrieve more items.
Type: Boolean

 ** Marker **
When IsTruncated is true, this element is present and contains the value to use for the Marker parameter in a subsequent pagination request.
Type: String

 **ServiceSpecificCredentials.member.N**
A list of structures that each contain details about a service-specific credential.
Type: Array of [ServiceSpecificCredentialMetadata](API_ServiceSpecificCredentialMetadata.md) objects

## Errors
<a name="API_ListServiceSpecificCredentials_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** NoSuchEntity **
The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
HTTP Status Code: 404

 ** NotSupportedService **
The specified service does not support service-specific credentials.
HTTP Status Code: 404

## Examples
<a name="API_ListServiceSpecificCredentials_Examples"></a>

### Example
<a name="API_ListServiceSpecificCredentials_Example_1"></a>

The following example shows how to get the list of all service-specific credentials for the IAM user named Anika.

#### Sample Request
<a name="API_ListServiceSpecificCredentials_Example_1_Request"></a>

```
https://iam.amazonaws.com/?Action=ListServiceSpecificCredentials
&UserName=anika
&Version=2010-05-08
&AUTHPARAMS
```

#### Sample Response
<a name="API_ListServiceSpecificCredentials_Example_1_Response"></a>

```
<ListServiceSpecificCredentialsResponse xmlns="https://iam.amazonaws.com/doc/2010-05-08/">
  <ListServiceSpecificCredentialsResult>
    <ServiceSpecificCredentials>
      <member>
        <ServiceName>codecommit.amazonaws.com</ServiceName>
        <UserName>anika</UserName>
        <ServiceUserName>anika-at-123456789012</ServiceUserName>
        <ServiceSpecificCredentialId>ACCA12345ABCDEXAMPLE</ServiceSpecificCredentialId>
        <Status>Active</Status>
        <CreateDate>2016-11-01T17:44:54Z</CreateDate>
      </member>
      <member>
        <ServiceName>codecommit.amazonaws.com</ServiceName>
        <UserName>anika</UserName>
        <ServiceUserName>anika+1-at-123456789012</ServiceUserName>
        <ServiceSpecificCredentialId>ACCA67890FGHIEXAMPLE</ServiceSpecificCredentialId>
        <Status>Active</Status>
        <CreateDate>2016-11-01T18:22:26Z</CreateDate>
      </member>
    </ServiceSpecificCredentials>
  </ListServiceSpecificCredentialsResult>
  <ResponseMetadata>
    <RequestId>EXAMPLE8-90ab-cdef-fedc-ba987EXAMPLE</RequestId>
  </ResponseMetadata>
</ListServiceSpecificCredentialsResponse>
```

## See Also
<a name="API_ListServiceSpecificCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/ListServiceSpecificCredentials)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/ListServiceSpecificCredentials)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/ListServiceSpecificCredentials)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/ListServiceSpecificCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/ListServiceSpecificCredentials)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/ListServiceSpecificCredentials)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/ListServiceSpecificCredentials)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/ListServiceSpecificCredentials)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/ListServiceSpecificCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/ListServiceSpecificCredentials)
