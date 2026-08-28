---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListDevices.html
---

# ListDevices
<a name="API_ListDevices"></a>

Gets information about unique device types.

## Request Syntax
<a name="API_ListDevices_RequestSyntax"></a>

```
{
   "arn": "{{string}}",
   "filters": [
      {
         "attribute": "{{string}}",
         "operator": "{{string}}",
         "values": [ "{{string}}" ]
      }
   ],
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListDevices_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [arn](#API_ListDevices_RequestSyntax) **   <a name="devicefarm-ListDevices-request-arn"></a>
The Amazon Resource Name (ARN) of the project.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: No

 ** [filters](#API_ListDevices_RequestSyntax) **   <a name="devicefarm-ListDevices-request-filters"></a>
Used to select a set of devices. A filter is made up of an attribute, an operator, and one or more values.
+ Attribute: The aspect of a device such as platform or model used as the selection criteria in a device filter.

  Allowed values include:
  + ARN: The Amazon Resource Name (ARN) of the device (for example, `arn:aws:devicefarm:us-west-2::device:12345Example`).
  + PLATFORM: The device platform. Valid values are ANDROID or IOS.
  + OS\_VERSION: The operating system version (for example, 10.3.2).
  + MODEL: The device model (for example, iPad 5th Gen).
  + AVAILABILITY: The current availability of the device. Valid values are AVAILABLE, HIGHLY\_AVAILABLE, BUSY, or TEMPORARY\_NOT\_AVAILABLE.
  + FORM\_FACTOR: The device form factor. Valid values are PHONE or TABLET.
  + MANUFACTURER: The device manufacturer (for example, Apple).
  + REMOTE\_ACCESS\_ENABLED: Whether the device is enabled for remote access. Valid values are TRUE or FALSE.
  + REMOTE\_DEBUG\_ENABLED: Whether the device is enabled for remote debugging. Valid values are TRUE or FALSE. Because remote debugging is [no longer supported](https://docs.aws.amazon.com/devicefarm/latest/developerguide/history.html), this attribute is ignored.
  + INSTANCE\_ARN: The Amazon Resource Name (ARN) of the device instance.
  + INSTANCE\_LABELS: The label of the device instance.
  + FLEET\_TYPE: The fleet type. Valid values are PUBLIC or PRIVATE.
+ Operator: The filter operator.
  + The EQUALS operator is available for every attribute except INSTANCE\_LABELS.
  + The CONTAINS operator is available for the INSTANCE\_LABELS and MODEL attributes.
  + The IN and NOT\_IN operators are available for the ARN, OS\_VERSION, MODEL, MANUFACTURER, and INSTANCE\_ARN attributes.
  + The LESS\_THAN, GREATER\_THAN, LESS\_THAN\_OR\_EQUALS, and GREATER\_THAN\_OR\_EQUALS operators are also available for the OS\_VERSION attribute.
+ Values: An array of one or more filter values.
  + The IN and NOT\_IN operators take a values array that has one or more elements.
  + The other operators require an array with a single element.
  + In a request, the AVAILABILITY attribute takes the following values: AVAILABLE, HIGHLY\_AVAILABLE, BUSY, or TEMPORARY\_NOT\_AVAILABLE.
Type: Array of [DeviceFilter](API_DeviceFilter.md) objects
Required: No

 ** [nextToken](#API_ListDevices_RequestSyntax) **   <a name="devicefarm-ListDevices-request-nextToken"></a>
An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_ListDevices_ResponseSyntax"></a>

```
{
   "devices": [
      {
         "arn": "string",
         "availability": "string",
         "carrier": "string",
         "cpu": {
            "architecture": "string",
            "clock": number,
            "frequency": "string"
         },
         "fleetName": "string",
         "fleetType": "string",
         "formFactor": "string",
         "heapSize": number,
         "image": "string",
         "instances": [
            {
               "arn": "string",
               "deviceArn": "string",
               "instanceProfile": {
                  "arn": "string",
                  "description": "string",
                  "excludeAppPackagesFromCleanup": [ "string" ],
                  "name": "string",
                  "packageCleanup": boolean,
                  "rebootAfterUse": boolean
               },
               "labels": [ "string" ],
               "status": "string",
               "udid": "string"
            }
         ],
         "manufacturer": "string",
         "memory": number,
         "model": "string",
         "modelId": "string",
         "name": "string",
         "os": "string",
         "platform": "string",
         "radio": "string",
         "remoteAccessEnabled": boolean,
         "remoteDebugEnabled": boolean,
         "resolution": {
            "height": number,
            "width": number
         }
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListDevices_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [devices](#API_ListDevices_ResponseSyntax) **   <a name="devicefarm-ListDevices-response-devices"></a>
Information about the devices.
Type: Array of [Device](API_Device.md) objects

 ** [nextToken](#API_ListDevices_ResponseSyntax) **   <a name="devicefarm-ListDevices-response-nextToken"></a>
If the number of items that are returned is significantly large, this is an identifier that is also returned. It can be used in a subsequent call to this operation to return the next set of items in the list.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.

## Errors
<a name="API_ListDevices_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ArgumentException **
An invalid argument was specified.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** LimitExceededException **
A limit was exceeded.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** NotFoundException **
The specified entity was not found.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** ServiceAccountException **
There was a problem with the service account.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

## See Also
<a name="API_ListDevices_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devicefarm-2015-06-23/ListDevices)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devicefarm-2015-06-23/ListDevices)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/ListDevices)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devicefarm-2015-06-23/ListDevices)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/ListDevices)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devicefarm-2015-06-23/ListDevices)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devicefarm-2015-06-23/ListDevices)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devicefarm-2015-06-23/ListDevices)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devicefarm-2015-06-23/ListDevices)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/ListDevices)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
