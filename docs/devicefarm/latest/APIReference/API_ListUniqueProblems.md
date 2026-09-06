---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_ListUniqueProblems.html
---

# ListUniqueProblems
<a name="API_ListUniqueProblems"></a>

Gets information about unique problems, such as exceptions or crashes.

Unique problems are defined as a single instance of an error across a run, job, or suite. For example, if a call in your application consistently raises an exception (`OutOfBoundsException in MyActivity.java:386`), `ListUniqueProblems` returns a single entry instead of many individual entries for that exception.

## Request Syntax
<a name="API_ListUniqueProblems_RequestSyntax"></a>

```
{
   "arn": "{{string}}",
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListUniqueProblems_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [arn](#API_ListUniqueProblems_RequestSyntax) **   <a name="devicefarm-ListUniqueProblems-request-arn"></a>
The unique problems' ARNs.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: Yes

 ** [nextToken](#API_ListUniqueProblems_RequestSyntax) **   <a name="devicefarm-ListUniqueProblems-request-nextToken"></a>
An identifier that was returned from the previous call to this operation, which can be used to return the next set of items in the list.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_ListUniqueProblems_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "uniqueProblems": {
      "string" : [
         {
            "message": "string",
            "problems": [
               {
                  "device": {
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
                  },
                  "job": {
                     "arn": "string",
                     "name": "string"
                  },
                  "message": "string",
                  "result": "string",
                  "run": {
                     "arn": "string",
                     "name": "string"
                  },
                  "suite": {
                     "arn": "string",
                     "name": "string"
                  },
                  "test": {
                     "arn": "string",
                     "name": "string"
                  }
               }
            ]
         }
      ]
   }
}
```

## Response Elements
<a name="API_ListUniqueProblems_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListUniqueProblems_ResponseSyntax) **   <a name="devicefarm-ListUniqueProblems-response-nextToken"></a>
If the number of items that are returned is significantly large, this is an identifier that is also returned. It can be used in a subsequent call to this operation to return the next set of items in the list.
Type: String
Length Constraints: Minimum length of 4. Maximum length of 1024.

 ** [uniqueProblems](#API_ListUniqueProblems_ResponseSyntax) **   <a name="devicefarm-ListUniqueProblems-response-uniqueProblems"></a>
Information about the unique problems.
Allowed values include:
+ PENDING
+ PASSED
+ WARNED
+ FAILED
+ SKIPPED
+ ERRORED
+ STOPPED
Type: String to array of [UniqueProblem](API_UniqueProblem.md) objects map
Valid Keys: `PENDING | PASSED | WARNED | FAILED | SKIPPED | ERRORED | STOPPED`

## Errors
<a name="API_ListUniqueProblems_Errors"></a>

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
<a name="API_ListUniqueProblems_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devicefarm-2015-06-23/ListUniqueProblems)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devicefarm-2015-06-23/ListUniqueProblems)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/ListUniqueProblems)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devicefarm-2015-06-23/ListUniqueProblems)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/ListUniqueProblems)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devicefarm-2015-06-23/ListUniqueProblems)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devicefarm-2015-06-23/ListUniqueProblems)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devicefarm-2015-06-23/ListUniqueProblems)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devicefarm-2015-06-23/ListUniqueProblems)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/ListUniqueProblems)
