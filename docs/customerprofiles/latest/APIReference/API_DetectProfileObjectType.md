---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_DetectProfileObjectType.html
---

# DetectProfileObjectType
<a name="API_connect-customer-profiles_DetectProfileObjectType"></a>

The process of detecting profile object type mapping by using given objects.

## Request Syntax
<a name="API_connect-customer-profiles_DetectProfileObjectType_RequestSyntax"></a>

```
POST /domains/{{DomainName}}/detect/object-types HTTP/1.1
Content-type: application/json

{
   "Objects": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_connect-customer-profiles_DetectProfileObjectType_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_DetectProfileObjectType_RequestSyntax) **   <a name="connect-connect-customer-profiles_DetectProfileObjectType-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_DetectProfileObjectType_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Objects](#API_connect-customer-profiles_DetectProfileObjectType_RequestSyntax) **   <a name="connect-connect-customer-profiles_DetectProfileObjectType-request-Objects"></a>
A string that is serialized from a JSON object.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Length Constraints: Minimum length of 1. Maximum length of 256000.
Required: Yes

## Response Syntax
<a name="API_connect-customer-profiles_DetectProfileObjectType_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DetectedProfileObjectTypes": [
      {
         "Fields": {
            "string" : {
               "ContentType": "string",
               "Source": "string",
               "Target": "string"
            }
         },
         "Keys": {
            "string" : [
               {
                  "FieldNames": [ "string" ],
                  "StandardIdentifiers": [ "string" ]
               }
            ]
         },
         "SourceLastUpdatedTimestampFormat": "string"
      }
   ]
}
```

## Response Elements
<a name="API_connect-customer-profiles_DetectProfileObjectType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DetectedProfileObjectTypes](#API_connect-customer-profiles_DetectProfileObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_DetectProfileObjectType-response-DetectedProfileObjectTypes"></a>
Detected `ProfileObjectType` mappings from given objects. A maximum of one mapping is supported.
Type: Array of [DetectedProfileObjectType](API_connect-customer-profiles_DetectedProfileObjectType.md) objects

## Errors
<a name="API_connect-customer-profiles_DetectProfileObjectType_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** BadRequestException **
The input you provided is invalid.
HTTP Status Code: 400

 ** InternalServerException **
An internal service error occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource does not exist, or access was denied.
HTTP Status Code: 404

 ** ThrottlingException **
You exceeded the maximum number of requests.
HTTP Status Code: 429

## See Also
<a name="API_connect-customer-profiles_DetectProfileObjectType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/DetectProfileObjectType)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/DetectProfileObjectType)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/DetectProfileObjectType)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/DetectProfileObjectType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/DetectProfileObjectType)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/DetectProfileObjectType)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/DetectProfileObjectType)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/DetectProfileObjectType)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/DetectProfileObjectType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/DetectProfileObjectType)
