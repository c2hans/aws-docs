---
source_url: https://docs.aws.amazon.com/AmazonCloudWatchLogs/latest/APIReference/API_ListAnomalies.html
---

# ListAnomalies
<a name="API_ListAnomalies"></a>

Returns a list of anomalies that log anomaly detectors have found. For details about the structure format of each anomaly object that is returned, see the example in this section.

## Request Syntax
<a name="API_ListAnomalies_RequestSyntax"></a>

```
{
   "anomalyDetectorArn": "{{string}}",
   "limit": {{number}},
   "nextToken": "{{string}}",
   "suppressionState": "{{string}}"
}
```

## Request Parameters
<a name="API_ListAnomalies_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [anomalyDetectorArn](#API_ListAnomalies_RequestSyntax) **   <a name="CWL-ListAnomalies-request-anomalyDetectorArn"></a>
Use this to optionally limit the results to only the anomalies found by a certain anomaly detector.
Type: String
Length Constraints: Minimum length of 1.
Pattern: `[\w#+=/:,.@-]*`
Required: No

 ** [limit](#API_ListAnomalies_RequestSyntax) **   <a name="CWL-ListAnomalies-request-limit"></a>
The maximum number of items to return. If you don't specify a value, the default maximum value of 50 items is used.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 50.
Required: No

 ** [nextToken](#API_ListAnomalies_RequestSyntax) **   <a name="CWL-ListAnomalies-request-nextToken"></a>
The token for the next set of items to return. The token expires after 24 hours.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [suppressionState](#API_ListAnomalies_RequestSyntax) **   <a name="CWL-ListAnomalies-request-suppressionState"></a>
You can specify this parameter if you want to the operation to return only anomalies that are currently either suppressed or unsuppressed.
Type: String
Valid Values: `SUPPRESSED | UNSUPPRESSED`
Required: No

## Response Syntax
<a name="API_ListAnomalies_ResponseSyntax"></a>

```
{
   "anomalies": [
      {
         "active": boolean,
         "anomalyDetectorArn": "string",
         "anomalyId": "string",
         "description": "string",
         "firstSeen": number,
         "histogram": {
            "string" : number
         },
         "isPatternLevelSuppression": boolean,
         "lastSeen": number,
         "logGroupArnList": [ "string" ],
         "logSamples": [
            {
               "message": "string",
               "timestamp": number
            }
         ],
         "patternId": "string",
         "patternRegex": "string",
         "patternString": "string",
         "patternTokens": [
            {
               "dynamicTokenPosition": number,
               "enumerations": {
                  "string" : number
               },
               "inferredTokenName": "string",
               "isDynamic": boolean,
               "tokenString": "string"
            }
         ],
         "priority": "string",
         "state": "string",
         "suppressed": boolean,
         "suppressedDate": number,
         "suppressedUntil": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAnomalies_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [anomalies](#API_ListAnomalies_ResponseSyntax) **   <a name="CWL-ListAnomalies-response-anomalies"></a>
An array of structures, where each structure contains information about one anomaly that a log anomaly detector has found.
Type: Array of [Anomaly](API_Anomaly.md) objects

 ** [nextToken](#API_ListAnomalies_ResponseSyntax) **   <a name="CWL-ListAnomalies-response-nextToken"></a>
The token for the next set of items to return. The token expires after 24 hours.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_ListAnomalies_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
A parameter is specified incorrectly.
HTTP Status Code: 400

 ** OperationAbortedException **
Multiple concurrent requests to update the same resource were in conflict.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource does not exist.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service cannot complete the request.
HTTP Status Code: 500

## Examples
<a name="API_ListAnomalies_Examples"></a>

### To retrieve a list of anomalies found by logs anomaly detectors
<a name="API_ListAnomalies_Example_1"></a>

This example illustrates one usage of ListAnomalies.

#### Sample Request
<a name="API_ListAnomalies_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: logs.<region>.<domain>
X-Amz-Date: <DATE>
Authorization: AWS4-HMAC-SHA256 Credential=<Credential>, SignedHeaders=content-type;date;host;user-agent;x-amz-date;x-amz-target;x-amzn-requestid, Signature=<Signature>
User-Agent: <UserAgentString>
Accept: application/json
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Connection: Keep-Alive
X-Amz-Target: Logs_20140328.ListAnomalies
{
   "anomalyDetectorArn": "arn:aws:logs:us-west-1:123456789012:anomaly-detector:EXAMPLE-1234-5678-abcd-111111111111",
   "limit": 50,
}
```

#### Sample Response
<a name="API_ListAnomalies_Example_1_Response"></a>

```
{
    "anomalies": [
        {
            "active": false,
            "anomalyDetectorArn": "arn:aws:logs:us-west-1:123456789012:anomaly-detector:EXAMPLE-1234-5678-abcd-111111111111",
            "anomalyId": "EXAMPLE-529d-4e1e-bea9-123EXAMPLE",
            "description": "Count of ErrorCode: 200 at token: 9 deviated expected by: 20.00%",
            "firstSeen": 1698488280000,
            "histogram": {
                "1698487995000": 2,
                "1698488285000": 4,
                "1698488295000": 1,
                "1698488300000": 1,
                "1698488305000": 4
            },
            "isPatternLevelSuppression": false,
            "lastSeen": 1698488580000,
            "logGroupArnList": [
                "arn:aws:logs:us-east-1:123456789012:log-group:/aws/lambda/my-log-group-name"
            ],
            "logSamples": [
                {
                    "message": "2023-10-28T10:18:18.959Z\EXAMPLE-4e26-41d8-8b54-EXAMPLE\tINFO\tResponse: 200 https://global.console.aws.amazon.com/EXAMPLEURL",
                    "timestamp": 1698488298959
                }
            ],
            "patternId": "EXAMPLE86827f77073836412345678",
            "patternRegex": ".*\\Q\t\\E.*\\Q\tINFO\tResponse: \\E.*\\Q https:\\E.*\\Q=\\E.*\\Q=\\E.*\\Q=\\E.*\\Q\n\\E",
            "patternString": "<*>\t<*>\tINFO\tResponse: <*> https:<*>=<*>=<*>=<*>\n",
            "patternTokens": [
                {
                    "dynamicTokenPosition": 1,
                    "enumerations": {
                        "2023-10-28T10:18:08.420Z": 2,
                        "2023-10-28T10:18:18.959Z": 1,
                        "2023-10-28T10:18:20.260Z": 1,
                        "2023-10-28T10:18:25.440Z": 1,
                        "2023-10-28T10:18:27.508Z": 1
                    },
                    "isDynamic": true,
                    "tokenString": "<*>"
                },
                {
                    "dynamicTokenPosition": 0,
                    "enumerations": {},
                    "isDynamic": false,
                    "tokenString": "\t"
                },
                {
                    "dynamicTokenPosition": 2,
                    "enumerations": {
                        "4766bcdd-4e26-41d8-8b54-fa0ae43f6201": 6
                    },
                    "isDynamic": true,
                    "tokenString": "<*>"
                },
                {
                    "dynamicTokenPosition": 0,
                    "enumerations": {},
                    "isDynamic": false,
                    "tokenString": "\t"
                },
                {
                    "dynamicTokenPosition": 0,
                    "enumerations": {},
                    "isDynamic": false,
                    "tokenString": "INFO"
                },
                {
                    "dynamicTokenPosition": 0,
                    "enumerations": {},
                    "isDynamic": false,
                    "tokenString": "\t"
                },
                {
                    "dynamicTokenPosition": 0,
                    "enumerations": {},
                    "isDynamic": false,
                    "tokenString": "Response"
                },
                {
                    "dynamicTokenPosition": 0,
                    "enumerations": {},
                    "isDynamic": false,
                    "tokenString": ":"
                },
                {
                    "dynamicTokenPosition": 0,
                    "enumerations": {},
                    "isDynamic": false,
                    "tokenString": " "
                },
                {
                    "dynamicTokenPosition": 3,
                    "enumerations": {
                        "200": 6
                    },
                    "isDynamic": true,
                    "tokenString": "<*>"
                },
                {
                    "dynamicTokenPosition": 0,
                    "enumerations": {},
                    "isDynamic": false,
                    "tokenString": " "
                },
                {
                    "dynamicTokenPosition": 0,
                    "enumerations": {},
                    "isDynamic": false,
                    "tokenString": "https"
                },
                {
                    "dynamicTokenPosition": 0,
                    "enumerations": {},
                    "isDynamic": false,
                    "tokenString": ":"
                },
                {
                    "dynamicTokenPosition": 4,
                    "enumerations": {
                        "//global.console.aws.amazon.com/EXAMPLEURL": 1,
                        "//prod.EXAMPLEURL2": 5
                    },
                    "isDynamic": true,
                    "tokenString": "<*>"
                },
                {
                    "dynamicTokenPosition": 0,
                    "enumerations": {},
                    "isDynamic": false,
                    "tokenString": "="
                },
                {
                    "dynamicTokenPosition": 5,
                    "enumerations": {
                        "%40amzn%2Faws-ccx-regions-availability&majorVersion": 1,
                        "info&message": 5
                    },
                    "isDynamic": true,
                    "tokenString": "<*>"
                },
                {
                    "dynamicTokenPosition": 0,
                    "enumerations": {},
                    "isDynamic": false,
                    "tokenString": "="
                },
                {
                    "dynamicTokenPosition": 6,
                    "enumerations": {
                        "1&versionId": 1,
                        "checkForCookieConsent&payload": 3,
                        "geolocationLatency&payload": 1,
                        "uiMounted&payload": 1
                    },
                    "isDynamic": true,
                    "tokenString": "<*>"
                },
                {
                    "dynamicTokenPosition": 0,
                    "enumerations": {},
                    "isDynamic": false,
                    "tokenString": "="
                },
               {
                    "dynamicTokenPosition": 0,
                    "enumerations": {},
                    "isDynamic": false,
                    "tokenString": "\n"
                }
            ],
            "priority": "LOW",
            "state": "Active",
            "suppressed": false,
            "suppressedDate": 0,
            "suppressedUntil": 0
        },
        {
            "active": false,
            "anomalyDetectorArn": "arn:aws:logs:us-west-1:123456789012:anomaly-detector:EXAMPLE-1234-5678-abcd-111111111111",
            "anomalyId": "EXAMPLE-09d4-4286-9cd3-EXAMPLE",
            "description": "Count of ErrorCode: 200 at token: 9 deviated expected by: 95.12%",
            "firstSeen": 1698392040000,
            "histogram": {
                "1698392035000": 17,
                "1698392040000": 5
            },
            "isPatternLevelSuppression": true,
            "lastSeen": 1698392340000,
            "logGroupArnList": [
                "arn:aws:logs:us-east-1:123456789012:log-group:another-log-group"
            ],
            "logSamples": [
                {
                    "message": "2023-10-27T07:33:56.178Z\tb3c81837-ead3-46ac-9334-68fa05453033\tINFO\tResponse: 200 https://EXAMPLE-URL-2",
                    "timestamp": 1698392036178
                }
            ],
            "patternId": "9f2e9e2844e41728651fb229351c90e0",
            "patternRegex": ".*\\Q\t\\E.*\\Q\tINFO\tResponse: \\E.*\\Q https:\\E.*\\Q\n\\E",
            "patternString": "<*>\t<*>\tINFO\tResponse: <*> https:<*>\n",
            "patternTokens": [
                {
                    "dynamicTokenPosition": 1,
                    "enumerations": {
                        "2023-10-27T07:33:56.238Z": 1,
                        "2023-10-27T07:33:56.253Z": 1,
                        "2023-10-27T07:33:56.274Z": 1,
                        "2023-10-27T07:33:56.295Z": 1,
                        "2023-10-27T07:34:01.929Z": 1
                    },
                    "isDynamic": true,
                    "tokenString": "<*>"
                },
                {
                    "dynamicTokenPosition": 0,
                    "enumerations": {},
                    "isDynamic": false,
                    "tokenString": "\t"
                },
                {
                    "dynamicTokenPosition": 2,
                    "enumerations": {
                        "b3c81837-ead3-46ac-9334-68fa05453033": 22
                    },
                    "isDynamic": true,
                    "tokenString": "<*>"
                },
                {
                    "dynamicTokenPosition": 0,
                    "enumerations": {},
                    "isDynamic": false,
                    "tokenString": "\t"
                },
                {
                    "dynamicTokenPosition": 0,
                    "enumerations": {},
                    "isDynamic": false,
                    "tokenString": "INFO"
                },
                {
                    "dynamicTokenPosition": 0,
                    "enumerations": {},
                    "isDynamic": false,
                    "tokenString": "\t"
                },
                {
                    "dynamicTokenPosition": 0,
                    "enumerations": {},
                    "isDynamic": false,
                    "tokenString": "Response"
                },
                {
                    "dynamicTokenPosition": 0,
                    "enumerations": {},
                    "isDynamic": false,
                    "tokenString": ":"
                },
                {
                    "dynamicTokenPosition": 0,
                    "enumerations": {},
                    "isDynamic": false,
                    "tokenString": " "
                },
                {
                    "dynamicTokenPosition": 3,
                    "enumerations": {
                        "200": 22
                    },
                    "isDynamic": true,
                    "tokenString": "<*>"
                },
                {
                    "dynamicTokenPosition": 0,
                    "enumerations": {},
                    "isDynamic": false,
                    "tokenString": " "
                },
                {
                    "dynamicTokenPosition": 0,
                    "enumerations": {},
                    "isDynamic": false,
                    "tokenString": "https"
                },
                {
                    "dynamicTokenPosition": 0,
                    "enumerations": {},
                    "isDynamic": false,
                    "tokenString": ":"
                },
                {
                    "dynamicTokenPosition": 4,
                    "enumerations": {
                        "//EXAMPLE-URL-1": 12,
                        "//EXAMPLE-URL-2": 1,
                        "//EXAMPLE-URL-2": 6,
                        "//EXAMPLE-URL-3": 3
                    },
                    "isDynamic": true,
                    "tokenString": "<*>"
                },
                {
                    "dynamicTokenPosition": 0,
                    "enumerations": {},
                    "isDynamic": false,
                    "tokenString": "\n"
                }
            ],
            "priority": "LOW",
            "state": "Active",
            "suppressed": true,
            "suppressedDate": 0,
            "suppressedUntil": 1702393208766
        },
```

## See Also
<a name="API_ListAnomalies_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/logs-2014-03-28/ListAnomalies)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/logs-2014-03-28/ListAnomalies)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/logs-2014-03-28/ListAnomalies)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/logs-2014-03-28/ListAnomalies)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/logs-2014-03-28/ListAnomalies)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/logs-2014-03-28/ListAnomalies)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/logs-2014-03-28/ListAnomalies)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/logs-2014-03-28/ListAnomalies)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/ListAnomalies)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/logs-2014-03-28/ListAnomalies)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CloudWatch Logs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonCloudWatchLogs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
