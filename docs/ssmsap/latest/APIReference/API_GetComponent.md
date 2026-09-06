---
source_url: https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_GetComponent.html
---

# GetComponent
<a name="API_GetComponent"></a>

Gets the component of an application registered with AWS Systems Manager for SAP.

## Request Syntax
<a name="API_GetComponent_RequestSyntax"></a>

```
POST /get-component HTTP/1.1
Content-type: application/json

{
   "ApplicationId": "{{string}}",
   "ComponentId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetComponent_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetComponent_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ApplicationId](#API_GetComponent_RequestSyntax) **   <a name="ssmsap-GetComponent-request-ApplicationId"></a>
The ID of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60.
Pattern: `[\w\d\.-]+`
Required: Yes

 ** [ComponentId](#API_GetComponent_RequestSyntax) **   <a name="ssmsap-GetComponent-request-ComponentId"></a>
The ID of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\d-]+`
Required: Yes

## Response Syntax
<a name="API_GetComponent_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Component": {
      "ApplicationId": "string",
      "Arn": "string",
      "AssociatedHost": {
         "Ec2InstanceId": "string",
         "Hostname": "string",
         "IpAddresses": [
            {
               "AllocationType": "string",
               "IpAddress": "string",
               "Primary": boolean
            }
         ],
         "OsVersion": "string"
      },
      "ChildComponents": [ "string" ],
      "ComponentId": "string",
      "ComponentType": "string",
      "DatabaseConnection": {
         "ConnectionIp": "string",
         "DatabaseArn": "string",
         "DatabaseConnectionMethod": "string"
      },
      "Databases": [ "string" ],
      "HdbVersion": "string",
      "Hosts": [
         {
            "EC2InstanceId": "string",
            "HostIp": "string",
            "HostName": "string",
            "HostRole": "string",
            "InstanceId": "string",
            "OsVersion": "string"
         }
      ],
      "LastUpdated": number,
      "ParentComponent": "string",
      "PrimaryHost": "string",
      "Resilience": {
         "ClusterStatus": "string",
         "EnqueueReplication": boolean,
         "HsrOperationMode": "string",
         "HsrReplicationMode": "string",
         "HsrTier": "string"
      },
      "SapFeature": "string",
      "SapHostname": "string",
      "SapKernelVersion": "string",
      "Sid": "string",
      "Status": "string",
      "SystemNumber": "string"
   },
   "Tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_GetComponent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Component](#API_GetComponent_ResponseSyntax) **   <a name="ssmsap-GetComponent-response-Component"></a>
The component of an application registered with AWS Systems Manager for SAP.
Type: [Component](API_Component.md) object

 ** [Tags](#API_GetComponent_ResponseSyntax) **   <a name="ssmsap-GetComponent-response-Tags"></a>
The tags of a component.
Type: String to string map
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_GetComponent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
An internal error has occurred.
HTTP Status Code: 500

 ** UnauthorizedException **
The request is not authorized.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetComponent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-sap-2018-05-10/GetComponent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-sap-2018-05-10/GetComponent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-sap-2018-05-10/GetComponent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-sap-2018-05-10/GetComponent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-sap-2018-05-10/GetComponent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-sap-2018-05-10/GetComponent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-sap-2018-05-10/GetComponent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-sap-2018-05-10/GetComponent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-sap-2018-05-10/GetComponent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-sap-2018-05-10/GetComponent)
