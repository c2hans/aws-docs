---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_UpdateKxEnvironmentNetwork.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# UpdateKxEnvironmentNetwork
<a name="API_UpdateKxEnvironmentNetwork"></a>

Updates environment network to connect to your internal network by using a transit gateway. This API supports request to create a transit gateway attachment from FinSpace VPC to your transit gateway ID and create a custom Route-53 outbound resolvers.

Once you send a request to update a network, you cannot change it again. Network update might require termination of any clusters that are running in the existing network.

## Request Syntax
<a name="API_UpdateKxEnvironmentNetwork_RequestSyntax"></a>

```
PUT /kx/environments/{{environmentId}}/network HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "customDNSConfiguration": [
      {
         "customDNSServerIP": "{{string}}",
         "customDNSServerName": "{{string}}"
      }
   ],
   "transitGatewayConfiguration": {
      "attachmentNetworkAclConfiguration": [
         {
            "cidrBlock": "{{string}}",
            "icmpTypeCode": {
               "code": {{number}},
               "type": {{number}}
            },
            "portRange": {
               "from": {{number}},
               "to": {{number}}
            },
            "protocol": "{{string}}",
            "ruleAction": "{{string}}",
            "ruleNumber": {{number}}
         }
      ],
      "routableCIDRSpace": "{{string}}",
      "transitGatewayID": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateKxEnvironmentNetwork_RequestParameters"></a>

The request uses the following URI parameters.

 ** [environmentId](#API_UpdateKxEnvironmentNetwork_RequestSyntax) **   <a name="finspace-UpdateKxEnvironmentNetwork-request-uri-environmentId"></a>
A unique identifier for the kdb environment.
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `^[a-zA-Z0-9]{1,26}$`
Required: Yes

## Request Body
<a name="API_UpdateKxEnvironmentNetwork_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_UpdateKxEnvironmentNetwork_RequestSyntax) **   <a name="finspace-UpdateKxEnvironmentNetwork-request-clientToken"></a>
A token that ensures idempotency. This token expires in 10 minutes.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `.*\S.*`
Required: No

 ** [customDNSConfiguration](#API_UpdateKxEnvironmentNetwork_RequestSyntax) **   <a name="finspace-UpdateKxEnvironmentNetwork-request-customDNSConfiguration"></a>
A list of DNS server name and server IP. This is used to set up Route-53 outbound resolvers.
Type: Array of [CustomDNSServer](API_CustomDNSServer.md) objects
Required: No

 ** [transitGatewayConfiguration](#API_UpdateKxEnvironmentNetwork_RequestSyntax) **   <a name="finspace-UpdateKxEnvironmentNetwork-request-transitGatewayConfiguration"></a>
Specifies the transit gateway and network configuration to connect the kdb environment to an internal network.
Type: [TransitGatewayConfiguration](API_TransitGatewayConfiguration.md) object
Required: No

## Response Syntax
<a name="API_UpdateKxEnvironmentNetwork_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "availabilityZoneIds": [ "string" ],
   "awsAccountId": "string",
   "creationTimestamp": number,
   "customDNSConfiguration": [
      {
         "customDNSServerIP": "string",
         "customDNSServerName": "string"
      }
   ],
   "dedicatedServiceAccountId": "string",
   "description": "string",
   "dnsStatus": "string",
   "environmentArn": "string",
   "environmentId": "string",
   "errorMessage": "string",
   "kmsKeyId": "string",
   "name": "string",
   "status": "string",
   "tgwStatus": "string",
   "transitGatewayConfiguration": {
      "attachmentNetworkAclConfiguration": [
         {
            "cidrBlock": "string",
            "icmpTypeCode": {
               "code": number,
               "type": number
            },
            "portRange": {
               "from": number,
               "to": number
            },
            "protocol": "string",
            "ruleAction": "string",
            "ruleNumber": number
         }
      ],
      "routableCIDRSpace": "string",
      "transitGatewayID": "string"
   },
   "updateTimestamp": number
}
```

## Response Elements
<a name="API_UpdateKxEnvironmentNetwork_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [availabilityZoneIds](#API_UpdateKxEnvironmentNetwork_ResponseSyntax) **   <a name="finspace-UpdateKxEnvironmentNetwork-response-availabilityZoneIds"></a>
The identifier of the availability zones where subnets for the environment are created.
Type: Array of strings
Length Constraints: Minimum length of 8. Maximum length of 12.
Pattern: `^[a-zA-Z0-9-]+$`

 ** [awsAccountId](#API_UpdateKxEnvironmentNetwork_ResponseSyntax) **   <a name="finspace-UpdateKxEnvironmentNetwork-response-awsAccountId"></a>
The unique identifier of the AWS account that is used to create the kdb environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `^[a-zA-Z0-9]{1,26}$`

 ** [creationTimestamp](#API_UpdateKxEnvironmentNetwork_ResponseSyntax) **   <a name="finspace-UpdateKxEnvironmentNetwork-response-creationTimestamp"></a>
The timestamp at which the kdb environment was created in FinSpace.
Type: Timestamp

 ** [customDNSConfiguration](#API_UpdateKxEnvironmentNetwork_ResponseSyntax) **   <a name="finspace-UpdateKxEnvironmentNetwork-response-customDNSConfiguration"></a>
A list of DNS server name and server IP. This is used to set up Route-53 outbound resolvers.
Type: Array of [CustomDNSServer](API_CustomDNSServer.md) objects

 ** [dedicatedServiceAccountId](#API_UpdateKxEnvironmentNetwork_ResponseSyntax) **   <a name="finspace-UpdateKxEnvironmentNetwork-response-dedicatedServiceAccountId"></a>
A unique identifier for the AWS environment infrastructure account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `^[a-zA-Z0-9]{1,26}$`

 ** [description](#API_UpdateKxEnvironmentNetwork_ResponseSyntax) **   <a name="finspace-UpdateKxEnvironmentNetwork-response-description"></a>
The description of the environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[a-zA-Z0-9. ]{1,1000}$`

 ** [dnsStatus](#API_UpdateKxEnvironmentNetwork_ResponseSyntax) **   <a name="finspace-UpdateKxEnvironmentNetwork-response-dnsStatus"></a>
The status of DNS configuration.
Type: String
Valid Values: `NONE | UPDATE_REQUESTED | UPDATING | FAILED_UPDATE | SUCCESSFULLY_UPDATED`

 ** [environmentArn](#API_UpdateKxEnvironmentNetwork_ResponseSyntax) **   <a name="finspace-UpdateKxEnvironmentNetwork-response-environmentArn"></a>
The ARN identifier of the environment.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws:finspace:[A-Za-z0-9_/.-]{0,63}:\d+:environment/[0-9A-Za-z_-]{1,128}$`

 ** [environmentId](#API_UpdateKxEnvironmentNetwork_ResponseSyntax) **   <a name="finspace-UpdateKxEnvironmentNetwork-response-environmentId"></a>
A unique identifier for the kdb environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `^[a-zA-Z0-9]{1,26}$`

 ** [errorMessage](#API_UpdateKxEnvironmentNetwork_ResponseSyntax) **   <a name="finspace-UpdateKxEnvironmentNetwork-response-errorMessage"></a>
Specifies the error message that appears if a flow fails.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `^[a-zA-Z0-9. ]{1,1000}$`

 ** [kmsKeyId](#API_UpdateKxEnvironmentNetwork_ResponseSyntax) **   <a name="finspace-UpdateKxEnvironmentNetwork-response-kmsKeyId"></a>
The KMS key ID to encrypt your data in the FinSpace environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[a-zA-Z-0-9-:\/]*$`

 ** [name](#API_UpdateKxEnvironmentNetwork_ResponseSyntax) **   <a name="finspace-UpdateKxEnvironmentNetwork-response-name"></a>
The name of the kdb environment.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`

 ** [status](#API_UpdateKxEnvironmentNetwork_ResponseSyntax) **   <a name="finspace-UpdateKxEnvironmentNetwork-response-status"></a>
The status of the kdb environment.
Type: String
Valid Values: `CREATE_REQUESTED | CREATING | CREATED | DELETE_REQUESTED | DELETING | DELETED | FAILED_CREATION | RETRY_DELETION | FAILED_DELETION | UPDATE_NETWORK_REQUESTED | UPDATING_NETWORK | FAILED_UPDATING_NETWORK | SUSPENDED`

 ** [tgwStatus](#API_UpdateKxEnvironmentNetwork_ResponseSyntax) **   <a name="finspace-UpdateKxEnvironmentNetwork-response-tgwStatus"></a>
The status of the network configuration.
Type: String
Valid Values: `NONE | UPDATE_REQUESTED | UPDATING | FAILED_UPDATE | SUCCESSFULLY_UPDATED`

 ** [transitGatewayConfiguration](#API_UpdateKxEnvironmentNetwork_ResponseSyntax) **   <a name="finspace-UpdateKxEnvironmentNetwork-response-transitGatewayConfiguration"></a>
The structure of the transit gateway and network configuration that is used to connect the kdb environment to an internal network.
Type: [TransitGatewayConfiguration](API_TransitGatewayConfiguration.md) object

 ** [updateTimestamp](#API_UpdateKxEnvironmentNetwork_ResponseSyntax) **   <a name="finspace-UpdateKxEnvironmentNetwork-response-updateTimestamp"></a>
The timestamp at which the kdb environment was updated.
Type: Timestamp

## Errors
<a name="API_UpdateKxEnvironmentNetwork_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There was a conflict with this action, and it could not be completed.
 ** reason **
The reason for the conflict exception.
HTTP Status Code: 409

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
One or more resources can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_UpdateKxEnvironmentNetwork_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/finspace-2021-03-12/UpdateKxEnvironmentNetwork)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/finspace-2021-03-12/UpdateKxEnvironmentNetwork)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/UpdateKxEnvironmentNetwork)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/finspace-2021-03-12/UpdateKxEnvironmentNetwork)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/UpdateKxEnvironmentNetwork)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/finspace-2021-03-12/UpdateKxEnvironmentNetwork)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/finspace-2021-03-12/UpdateKxEnvironmentNetwork)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/finspace-2021-03-12/UpdateKxEnvironmentNetwork)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/finspace-2021-03-12/UpdateKxEnvironmentNetwork)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/UpdateKxEnvironmentNetwork)
