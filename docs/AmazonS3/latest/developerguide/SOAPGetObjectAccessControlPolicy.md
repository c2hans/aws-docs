---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/developerguide/SOAPGetObjectAccessControlPolicy.html
---

# GetObjectAccessControlPolicy (SOAP API)
<a name="SOAPGetObjectAccessControlPolicy"></a>

**Note**
 SOAP APIs for Amazon S3 are not available for new customers, and are approaching End of Life (EOL) on August 31, 2025. We recommend that you use either the REST API or the AWS SDKs.

The `GetObjectAccessControlPolicy` operation fetches the access control policy for an object.

**Example**
This example retrieves the access control policy for the "Nelson" object from the "quotes" bucket.
`Sample Request`

```
1. <GetObjectAccessControlPolicy xmlns="https://doc.s3.amazonaws.com/2006-03-01">
2.   <Bucket>quotes</Bucket>
3.   <Key>Nelson</Key>
4.   <AWSAccessKeyId>AKIAIOSFODNN7EXAMPLE</AWSAccessKeyId>
5.   <Timestamp>2006-03-01T12:00:00.183Z</Timestamp>
6.   <Signature>Iuyz3d3P0aTou39dzbqaEXAMPLE=</Signature>
7. </GetObjectAccessControlPolicy>
```
`Sample Response`

```
 1. <AccessControlPolicy>
 2.   <Owner>
 3.     <ID>a9a7b886d6fd24a541bf9b1c61be666e9</ID>
 4.     <DisplayName>chriscustomer</DisplayName>
 5.   </Owner>
 6.   <AccessControlList>
 7.     <Grant>
 8.       <Grantee xsi:type="CanonicalUser">
 9.         <ID>a9a7b841bf9b1c61be666e9</ID>
10.         <DisplayName>chriscustomer</DisplayName>
11.       </Grantee>
12.       <Permission>FULL_CONTROL</Permission>
13.     </Grant>
14.     <Grant>
15.       <Grantee xsi:type="Group">
16.         <URI>http://acs.amazonaws.com/groups/global/AllUsers<URI>
17.       </Grantee>
18.       <Permission>READ</Permission>
19.     </Grant>
20.   </AccessControlList>
21. </AccessControlPolicy>
```

## Response Body
<a name="SOAPGetObjectAccessControlPolicyResponseBody"></a>

The response contains the access control policy for the bucket. For an explanation of this response, [SOAP Access Policy](https://docs.aws.amazon.com/AmazonS3/latest/userguide/SOAPAccessPolicy.html) .

## Access Control
<a name="SOAPGetObjectAccessControlPolicyAccessControl"></a>

You must have `READ_ACP` rights to the object in order to retrieve the access control policy for an object.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Simple Storage Service (S3). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonS3` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
