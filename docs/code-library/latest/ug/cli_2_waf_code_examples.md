---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cli_2_waf_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# AWS WAF Classic examples using AWS CLI
<a name="cli_2_waf_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with AWS WAF Classic.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `put-logging-configuration`
<a name="waf_PutLoggingConfiguration_cli_2_topic"></a>

The following code example shows how to use `put-logging-configuration`.

**AWS CLI**
**To create a logging configuration for the web ACL ARN with the specified Kinesis Firehose stream ARN**
The following `put-logging-configuration` example displays logging configuration for WAF with CloudFront.

```
aws waf put-logging-configuration \
    --logging-configuration {{ResourceArn=arn:aws:waf::123456789012:webacl/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111,LogDestinationConfigs=arn:aws:firehose:us-east-1:123456789012:deliverystream/aws-waf-logs-firehose-stream,RedactedFields=[]}}
```
Output:

```
{
    "LoggingConfiguration": {
        "ResourceArn": "arn:aws:waf::123456789012:webacl/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
        "LogDestinationConfigs": [
            "arn:aws:firehose:us-east-1:123456789012:deliverystream/aws-waf-logs-firehose-stream"
        ]
    }
}
```
For more information, see [Logging Web ACL traffic information](https://docs.aws.amazon.com/waf/latest/developerguide/classic-logging.html) in the *AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.
+  For API details, see [PutLoggingConfiguration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/put-logging-configuration.html) in *AWS CLI Command Reference*.

### `update-byte-match-set`
<a name="waf_UpdateByteMatchSet_cli_2_topic"></a>

The following code example shows how to use `update-byte-match-set`.

**AWS CLI**
**To update a byte match set**
The following `update-byte-match-set` example deletes a ByteMatchTuple object (filter) in a ByteMatchSet.

```
aws waf update-byte-match-set \
    --cli-binary-format {{raw-in-base64-out}} \
    --byte-match-set-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --change-token {{12cs345-67cd-890b-1cd2-c3a4567d89f1}} \
    --updates Action="DELETE",ByteMatchTuple={FieldToMatch={Type="HEADER",Data="referer"},TargetString="badrefer1",TextTransformation="NONE",PositionalConstraint="CONTAINS"}
```
Output:

```
{
    "ChangeToken": "12cs345-67cd-890b-1cd2-c3a4567d89f1"
}
```
For more information, see [Working with string match conditions](https://docs.aws.amazon.com/waf/latest/developerguide/classic-web-acl-string-conditions.html) in the *AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.
+  For API details, see [UpdateByteMatchSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-byte-match-set.html) in *AWS CLI Command Reference*.

### `update-ip-set`
<a name="waf_UpdateIpSet_cli_2_topic"></a>

The following code example shows how to use `update-ip-set`.

**AWS CLI**
**To update an IP set**
The following `update-ip-set` example updates an IPSet with an IPv4 address and deletes an IPv6 address.

```
aws waf update-ip-set \
    --ip-set-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --change-token {{12cs345-67cd-890b-1cd2-c3a4567d89f1}} \
    --updates Action="INSERT",IPSetDescriptor={Type="IPV4",Value="12.34.56.78/16"},Action="DELETE",IPSetDescriptor={Type="IPV6",Value="1111:0000:0000:0000:0000:0000:0000:0111/128"}
```
Output:

```
{
    "ChangeToken": "12cs345-67cd-890b-1cd2-c3a4567d89f1"
}
```
Alternatively, you can use a JSON file to specify the input, as shown in the following example.

```
aws waf update-ip-set \
    --ip-set-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --change-token {{12cs345-67cd-890b-1cd2-c3a4567d89f1}} \
    --updates {{file://change.json}}
```
Contents of `change.json`:

```
[
    {
        "Action": "INSERT",
        "IPSetDescriptor": {
            "Type": "IPV4",
            "Value": "12.34.56.78/16"
        }
    },
    {
        "Action": "DELETE",
        "IPSetDescriptor": {
            "Type": "IPV6",
            "Value": "1111:0000:0000:0000:0000:0000:0000:0111/128"
        }
    }
]
```
Output:

```
{
    "ChangeToken": "12cs345-67cd-890b-1cd2-c3a4567d89f1"
}
```
For more information, see [Working with IP match conditions](https://docs.aws.amazon.com/waf/latest/developerguide/classic-web-acl-ip-conditions.html) in the *AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.
+  For API details, see [UpdateIpSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-ip-set.html) in *AWS CLI Command Reference*.

### `update-rule`
<a name="waf_UpdateRule_cli_2_topic"></a>

The following code example shows how to use `update-rule`.

**AWS CLI**
**To update a rule**
The following `update-rule` example deletes a Predicate object in a rule.

```
aws waf update-rule \
    --rule-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --change-token {{12cs345-67cd-890b-1cd2-c3a4567d89f1}} \
    --updates Action="DELETE",Predicate={Negated=false,Type="ByteMatch",DataId="MyByteMatchSetID"}
```
Output:

```
{
    "ChangeToken": "12cs345-67cd-890b-1cd2-c3a4567d89f1"
}
```
For more information, see [Working with rules](https://docs.aws.amazon.com/waf/latest/developerguide/classic-web-acl-rules.html) in the *AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.
+  For API details, see [UpdateRule](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-rule.html) in *AWS CLI Command Reference*.

### `update-size-constraint-set`
<a name="waf_UpdateSizeConstraintSet_cli_2_topic"></a>

The following code example shows how to use `update-size-constraint-set`.

**AWS CLI**
**To update a size constraint set**
The following `update-size-constraint-set` example deletes a SizeConstraint object (filters) in a size constraint set.

```
aws waf update-size-constraint-set \
    --size-constraint-set-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --change-token {{12cs345-67cd-890b-1cd2-c3a4567d89f1}} \
    --updates Action="DELETE",SizeConstraint={FieldToMatch={Type="QUERY_STRING"},TextTransformation="NONE",ComparisonOperator="GT",Size=0}
```
Output:

```
{
    "ChangeToken": "12cs345-67cd-890b-1cd2-c3a4567d89f1"
}
```
For more information, see [Working with size constraint conditions](https://docs.aws.amazon.com/waf/latest/developerguide/classic-web-acl-size-conditions.html) in the *AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.
+  For API details, see [UpdateSizeConstraintSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-size-constraint-set.html) in *AWS CLI Command Reference*.

### `update-sql-injection-match-set`
<a name="waf_UpdateSqlInjectionMatchSet_cli_2_topic"></a>

The following code example shows how to use `update-sql-injection-match-set`.

**AWS CLI**
**To update a SQL Injection Match Set**
The following `update-sql-injection-match-set` example deletes a SqlInjectionMatchTuple object (filters) in a SQL injection match set.

```
aws waf update-sql-injection-match-set \
    --sql-injection-match-set-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --change-token {{12cs345-67cd-890b-1cd2-c3a4567d89f1}} \
    --updates Action="DELETE",SqlInjectionMatchTuple={FieldToMatch={Type="QUERY_STRING"},TextTransformation="URL_DECODE"}
```
Output:

```
{
    "ChangeToken": "12cs345-67cd-890b-1cd2-c3a4567d89f1"
}
```
For more information, see [Working with SQL injection match conditions](https://docs.aws.amazon.com/waf/latest/developerguide/classic-web-acl-sql-conditions.html) in the *AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.
+  For API details, see [UpdateSqlInjectionMatchSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-sql-injection-match-set.html) in *AWS CLI Command Reference*.

### `update-web-acl`
<a name="waf_UpdateWebAcl_cli_2_topic"></a>

The following code example shows how to use `update-web-acl`.

**AWS CLI**
**To update a web ACL**
The following `update-web-acl` example deletes an `ActivatedRule` object in a WebACL.

```
aws waf update-web-acl \
    --web-acl-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --change-token {{12cs345-67cd-890b-1cd2-c3a4567d89f1}} \
    --updates Action="DELETE",ActivatedRule='{Priority=1,RuleId="WAFRule-1-Example",Action={Type="ALLOW"},Type="REGULAR"}'
```
Output:

```
{
    "ChangeToken": "12cs345-67cd-890b-1cd2-c3a4567d89f1"
}
```
For more information, see [Working with Web ACLs](https://docs.aws.amazon.com/waf/latest/developerguide/classic-web-acl-working-with.html) in the *AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.
+  For API details, see [UpdateWebAcl](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-web-acl.html) in *AWS CLI Command Reference*.

### `update-xss-match-set`
<a name="waf_UpdateXssMatchSet_cli_2_topic"></a>

The following code example shows how to use `update-xss-match-set`.

**AWS CLI**
**To update an XSSMatchSet**
The following `update-xss-match-set` example deletes an XssMatchTuple object (filters) in an XssMatchSet.

```
aws waf update-xss-match-set \
    --xss-match-set-id {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}} \
    --change-token {{12cs345-67cd-890b-1cd2-c3a4567d89f1}} \
    --updates Action="DELETE",XssMatchTuple={FieldToMatch={Type="QUERY_STRING"},TextTransformation="URL_DECODE"}
```
Output:

```
{
    "ChangeToken": "12cs345-67cd-890b-1cd2-c3a4567d89f1"
}
```
For more information, see [Working with cross-site scripting match conditions](https://docs.aws.amazon.com/waf/latest/developerguide/classic-web-acl-xss-conditions.html) in the *AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Developer Guide*.
+  For API details, see [UpdateXssMatchSet](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/waf/update-xss-match-set.html) in *AWS CLI Command Reference*.
