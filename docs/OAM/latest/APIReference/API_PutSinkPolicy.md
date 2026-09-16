---
source_url: https://docs.aws.amazon.com/OAM/latest/APIReference/API_PutSinkPolicy.html
---

# PutSinkPolicy
<a name="API_PutSinkPolicy"></a>

Creates or updates the resource policy that grants permissions to source accounts to link to the monitoring account sink. When you create a sink policy, you can grant permissions to all accounts in an organization or to individual accounts.

You can also use a sink policy to limit the types of data that is shared. The six types of services with their respective resource types that you can allow or deny are:
+  **Metrics** - Specify with `AWS::CloudWatch::Metric`
+  **Log groups** - Specify with `AWS::Logs::LogGroup`
+  **Traces** - Specify with `AWS::XRay::Trace`
+  **Application Insights - Applications** - Specify with `AWS::ApplicationInsights::Application`
+  **Internet Monitor** - Specify with `AWS::InternetMonitor::Monitor`
+  **Application Signals** - Specify with `AWS::ApplicationSignals::Service` and `AWS::ApplicationSignals::ServiceLevelObjective`

See the examples in this section to see how to specify permitted source accounts and data types.

## Request Syntax
<a name="API_PutSinkPolicy_RequestSyntax"></a>

```
POST /PutSinkPolicy HTTP/1.1
Content-type: application/json

{
   "Policy": "{{string}}",
   "SinkIdentifier": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutSinkPolicy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_PutSinkPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Policy](#API_PutSinkPolicy_RequestSyntax) **   <a name="OAM-PutSinkPolicy-request-Policy"></a>
The JSON policy to use. If you are updating an existing policy, the entire existing policy is replaced by what you specify here.
The policy must be in JSON string format with quotation marks escaped and no newlines.
For examples of different types of policies, see the **Examples** section on this page.
Type: String
Required: Yes

 ** [SinkIdentifier](#API_PutSinkPolicy_RequestSyntax) **   <a name="OAM-PutSinkPolicy-request-SinkIdentifier"></a>
The ARN of the sink to attach this policy to.
Type: String
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_:\.\-\/]{0,2047}`
Required: Yes

## Response Syntax
<a name="API_PutSinkPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Policy": "string",
   "SinkArn": "string",
   "SinkId": "string"
}
```

## Response Elements
<a name="API_PutSinkPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Policy](#API_PutSinkPolicy_ResponseSyntax) **   <a name="OAM-PutSinkPolicy-response-Policy"></a>
The policy that you specified.
Type: String

 ** [SinkArn](#API_PutSinkPolicy_ResponseSyntax) **   <a name="OAM-PutSinkPolicy-response-SinkArn"></a>
The ARN of the sink.
Type: String

 ** [SinkId](#API_PutSinkPolicy_ResponseSyntax) **   <a name="OAM-PutSinkPolicy-response-SinkId"></a>
The random ID string that AWS generated as part of the sink ARN.
Type: String

## Errors
<a name="API_PutSinkPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceFault **
Unexpected error while processing the request. Retry the request.
 ** amznErrorType **
The name of the exception.
HTTP Status Code: 500

 ** InvalidParameterException **
A parameter is specified incorrectly.
 ** amznErrorType **
The name of the exception.
HTTP Status Code: 400

 ** MissingRequiredParameterException **
A required parameter is missing from the request.
 ** amznErrorType **
The name of the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The request references a resource that does not exist.
 ** amznErrorType **
The name of the exception.
HTTP Status Code: 404

## Examples
<a name="API_PutSinkPolicy_Examples"></a>

### Permission for all accounts in an organization
<a name="API_PutSinkPolicy_Example_1"></a>

The following example grants permission for all accounts in the organization `o-xxxxxxxxxxx` to be linked to this sink.

#### Sample Request
<a name="API_PutSinkPolicy_Example_1_Request"></a>

```
{
    "SinkIdentifier": "arn:aws:oam:us-west-1:111111111111:sink/abcd1234-a123-456a-a12b-a123b456c789",
    "Policy": "{ \"Version\": \"2012-10-17\",		 	 	  \"Statement\": [{ \"Action\": [\"oam:CreateLink\", \"oam:UpdateLink\"], \"Effect\": \"Allow\", \"Resource\": \"*\", \"Principal\": \"*\", \"Condition\": { \"StringEquals\": { \"aws:PrincipalOrgID\": \"o-xxxxxxxxxxx\" } } }]}" }
```

### Permission for individual accounts, allowing all resource types
<a name="API_PutSinkPolicy_Example_2"></a>

The following example grants permission for two specified accounts to be linked to this sink.

#### Sample Request
<a name="API_PutSinkPolicy_Example_2_Request"></a>

```
{
    "SinkIdentifier": "arn:aws:oam:us-west-1:111111111111:sink/abcd1234-a123-456a-a12b-a123b456c789",
    "Policy": "{\"Version\": \"2012-10-17\",		 	 	   \"Statement\": [{ \"Action\": [\"oam:CreateLink\", \"oam:UpdateLink\"], \"Effect\": \"Allow\", \"Resource\": \"*\", \"Principal\": { \"AWS\": [\"1111111111111\", \"222222222222\"]} }]  }"}
```

### Permission for individual accounts, allowing only metrics and logs to be shared
<a name="API_PutSinkPolicy_Example_3"></a>

The following example grants permission for two specified accounts to be linked to this sink. The link allows metrics and logs to be shared, but not traces.

#### Sample Request
<a name="API_PutSinkPolicy_Example_3_Request"></a>

```
{
    "SinkIdentifier": "arn:aws:oam:us-west-1:111111111111:sink/abcd1234-a123-456a-a12b-a123b456c789",
    "Policy": "{ \"Version\": \"2012-10-17\",		 	 	  \"Statement\": [{ \"Action\": [\"oam:CreateLink\", \"oam:UpdateLink\"], \"Effect\": \"Allow\",  \"Resource\": \"*\", \"Principal\": { \"AWS\": [\"1111111111111\", \"222222222222\"]}, \"Condition\": { \"ForAllValues:StringEquals\": { \"oam:ResourceTypes\": [ \"AWS::CloudWatch::Metric\", \"AWS::Logs::LogGroup\" ] }  }  }] }"
}
```

### Human-readable policy example- not for copying
<a name="API_PutSinkPolicy_Example_4"></a>

The following example will not work if used, but is included to show a human-readable version of a sink policy. This is the same policy as the previous example, and grants permission for two specified accounts to be linked to this sink. The link allows metrics and logs to be shared, but not traces.

#### Sample Request
<a name="API_PutSinkPolicy_Example_4_Request"></a>

```
{
    "SinkIdentifier": "arn:aws:oam:us-west-1:111111111111:sink/abcd1234-a123-456a-a12b-a123b456c789",
    "Policy": {
        "Version": "2012-10-17",
        "Statement": [{
            "Action": ["oam:CreateLink", "oam:UpdateLink"],
            "Effect": "Allow",
            "Resource": "*",
            "Principal": {
                "AWS": ["1111111111111", "222222222222"]
            },
            "Condition": {
                "ForAllValues:StringEquals": {
                    "oam:ResourceTypes": [
                        "AWS::CloudWatch::Metric",
                        "AWS::Logs::LogGroup"
                    ]
                }
            }
        }]
    }
}
```

### Permissions for full usage of Application Insights
<a name="API_PutSinkPolicy_Example_5"></a>

The following example policy will allow full usage of Application Insights. Full usage requires sharing of logs, metrics, traces, and application insights applications.

#### Sample Request
<a name="API_PutSinkPolicy_Example_5_Request"></a>

```
{
    "SinkIdentifier": "arn:aws:oam:us-west-1:111111111111:sink/abcd1234-a123-456a-a12b-a123b456c789",
    "Policy": {
        "Version": "2012-10-17",
        "Statement": [{
            "Action": ["oam:CreateLink", "oam:UpdateLink"],
            "Effect": "Allow",
            "Resource": "*",
            "Principal": {
                "AWS": ["1111111111111", "222222222222"]
            },
            "Condition": {
                "ForAllValues:StringEquals": {
                    "oam:ResourceTypes": [
                        "AWS::CloudWatch::Metric",
                        "AWS::Logs::LogGroup",
                        "AWS::XRay::Trace",
                        "AWS::ApplicationInsights::Application"
                    ]
                }
            }
        }]
    }
}
```

### Permissions for full usage of Internet Monitor
<a name="API_PutSinkPolicy_Example_6"></a>

The following example policy will allow full usage of Internet Monitor. Full usage requires sharing of logs, metrics, and internet monitors.

#### Sample Request
<a name="API_PutSinkPolicy_Example_6_Request"></a>

```
{
    "SinkIdentifier": "arn:aws:oam:us-west-1:111111111111:sink/abcd1234-a123-456a-a12b-a123b456c789",
    "Policy": {
        "Version": "2012-10-17",
        "Statement": [{
            "Action": ["oam:CreateLink", "oam:UpdateLink"],
            "Effect": "Allow",
            "Resource": "*",
            "Principal": {
                "AWS": ["1111111111111", "222222222222"]
            },
            "Condition": {
                "ForAllValues:StringEquals": {
                    "oam:ResourceTypes": [
                        "AWS::CloudWatch::Metric",
                        "AWS::Logs::LogGroup",
                        "AWS::InternetMonitor::Monitor"
                    ]
                }
            }
        }]
    }
}
```

### Permissions for full usage of Application Signals
<a name="API_PutSinkPolicy_Example_7"></a>

The following example policy will allow full usage of Application Signals. Full usage requires sharing of logs, metrics, traces, and Application Signals services and service level objectives.

#### Sample Request
<a name="API_PutSinkPolicy_Example_7_Request"></a>

```
{
    "SinkIdentifier": "arn:aws:oam:us-west-1:111111111111:sink/abcd1234-a123-456a-a12b-a123b456c789",
    "Policy": {
        "Version": "2012-10-17",
        "Statement": [{
            "Action": ["oam:CreateLink", "oam:UpdateLink"],
            "Effect": "Allow",
            "Resource": "*",
            "Principal": {
                "AWS": ["1111111111111", "222222222222"]
            },
            "Condition": {
                "ForAllValues:StringEquals": {
                    "oam:ResourceTypes": [
                        "AWS::CloudWatch::Metric",
                        "AWS::Logs::LogGroup",
                        "AWS::XRay::Trace",
                        "AWS::ApplicationSignals::Service",
                        "AWS::ApplicationSignals::ServiceLevelObjective"
                    ]
                }
            }
        }]
    }
}
```

## See Also
<a name="API_PutSinkPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/oam-2022-06-10/PutSinkPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/oam-2022-06-10/PutSinkPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/oam-2022-06-10/PutSinkPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/oam-2022-06-10/PutSinkPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/oam-2022-06-10/PutSinkPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/oam-2022-06-10/PutSinkPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/oam-2022-06-10/PutSinkPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/oam-2022-06-10/PutSinkPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/oam-2022-06-10/PutSinkPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/oam-2022-06-10/PutSinkPolicy)
