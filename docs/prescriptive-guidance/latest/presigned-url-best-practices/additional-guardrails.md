---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/presigned-url-best-practices/additional-guardrails.html
---

# Additional guardrails
<a name="additional-guardrails"></a>

When solution builders and users follow best practices for presigned requests, the requests provide a mechanism for giving users access to data. In addition, the ability to generate presigned requests doesn't give principals access that they didn't already have.

In that context, are additional controls necessary? You implement additional controls not to deny access, but to monitor usage, approve usage, set boundaries, and reduce the risk of user errors. These controls help you confirm that usage aligns with your business needs.

The following guardrails help you achieve this goal. Before you enable these controls, identify presigned requests to determine existing usage. This information helps you prepare for the impact of the guardrails on existing usage and plan exceptions where needed.

## Guardrail for s3:signatureAge
<a name="s3-signature-age"></a>

One defining characteristic of presigned requests is that they describe an expiration time. The signature for the request contains a date. This date is transmitted as an `X-Amz-Date` query string parameter for presigned URLs, and as a [Date or x-amz-date header ](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTCommonRequestHeaders.html)for a presigned POST.

Amazon S3 provides a condition key, [s3:signatureAge](https://docs.aws.amazon.com/AmazonS3/latest/API/bucket-policy-s3-sigv4-conditions.html), which you can use to limit the maximum time between the signed date and the effective expiration of the request. This condition can't increase the validity period, but it can reduce it.

In the following policy, the `s3:signatureAge` condition key limits presigned requests to 15 minutes of validity. The following examples all use 15 minutes to limit validity to a similar timeframe as standard signing supports.

The second statement from the policy denies any Signature Version 2 access. [This version of the signing protocol  is being deprecated](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingAWSSDK.html#UsingAWSSDK-sig2-deprecation), but it is still supported in some AWS Regions. We recommend that you explicitly block it before it is fully deprecated.

You can apply the following policy as an AWS Organizations service control policy (SCP). Users can still use presigned requests and deploy solutions that depend on those requests, as long as the time between signature generation and usage is less than 15 minutes. Depending on the implementation, this limitation might have no impact, it might cause a solution to become unusable, or it might cause occasional failures that can be retried.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyPresignedOver15Minutes",
      "Effect": "Deny",
      "Action": "s3:*",
      "Resource": "*",
      "Condition": {
        "NumericGreaterThan": {
          "s3:signatureAge": "900000"
        }
      }
    },
    {
      "Sid": "DenySignatureVersion2",
      "Effect": "Deny",
      "Action": "s3:*",
      "Resource": "*",
      "Condition": {
        "StringEquals": {
           "s3:signatureversion": "AWS"
        }
      }
    }
  ]
}
```

### Exceptions
<a name="exceptions.067ffc3d-89d3-5ca1-a827-d2a283f643da"></a>

If a solution requires a longer time before expiration and is therefore affected by the preceding policy, we recommend that you provide a method to approve exceptions. To avoid enumerating exceptions in an SCP, use [aws:PrincipalTag](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-principaltag), as in the following policy, to manage exceptions in a scalable way. Other AWS examples, such as the [AWS data perimeter](https://aws.amazon.com/identity/data-perimeters-on-aws/) policy examples, use this strategy.

If you implement an exception policy by using `aws:PrincipalTag`, you must control access to setting tags on principals. Tags of this type can come directly from principals, and an SCP can control them. A tag of this type can also come from [session tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html), which an identity provider (IdP) or AWS STS sets. Controlling access to `aws:PrincipalTag` can be complex. However, an organization that has experience using [attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) is likely to have the experience and controls to use `aws:PrincipalTag` for this use case.

In the following example, the `aws:PrincipalTag` condition creates an exception for any principal that has the named tag (`long-presigned-allowed`) assigned and set to `true`. With this exception, the policy doesn't apply the restriction on signature age.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyPresignedOver15Minutes",
      "Effect": "Deny",
      "Action": "s3:*",
      "Resource": "*",
      "Condition": {
        "NumericGreaterThan": {
          "s3:signatureAge": "900000"
        },
        "StringNotEquals": {
          "aws:PrincipalTag/long-presigned-allowed": "true"
        }
      }
    }
  ]
}
```

### Bucket policies
<a name="bucket-policies.00e78b1a-0be9-5183-a3cf-13a3cd64e516"></a>

You can apply bucket policies to all or selected buckets by using a policy as in the following example. Unlike an SCP, a bucket policy also targets [service principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#principal-services) usage. Appendix A doesn't document any expected service principal usage of presigned requests. However, if you want to enforce this limit for service principals as well, you can use the following policy. Also, unlike an SCP, a bucket policy can apply to principals in your management account.

ABAC-based exceptions work in bucket policies in the same way as in an SCP. A bucket policy might apply to principals outside your organization, so constrain ABAC exceptions to the principals for which ABAC controls apply.

In the following example, the `aws:PrincipalTag` condition in the first statement creates an exception for a principal that has the named tag (`long-presigned-allowed`) assigned and set to `true`. With this exception, the policy doesn't apply the restriction on signature age. The second statement applies this restriction to all principals outside the AWS organization that owns the bucket. Match the scope of this second statement to the ABAC controls that set the named tag for principals.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyPresignedOver15MinWithExceptions",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": "arn:aws:s3:::{bucket-name}/*",
      "Condition": {
        "NumericGreaterThan": {
          "s3:signatureAge": "900000"
        },
        "StringNotEquals": {
          "aws:PrincipalTag/long-presigned-allowed": "true"
        }
      }
    },
    {
      "Sid": "DenyPresignedOver15MinutesOutsideOrg",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": "arn:aws:s3:::{bucket-name}/*",
      "Condition": {
        "NumericGreaterThan": {
          "s3:signatureAge": "900000"
        },
        "StringNotEquals": {
          "aws:PrincipalOrgID": "${aws:ResourceOrgID}"
        }
      }
    }
  ]
}
```

## Resource control policies
<a name="rcps"></a>

You can apply a policy to buckets at scale by using [resource control policies (RCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html). Like service control policies (SCPs) and unlike bucket policies, RCPs do not target service principal usage. RCPs affect non-service principals from any account, but they do not affect resources in the management account. For more information, see the [AWS Organizations documentation.](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html#actions-not-restricted-by-rcps)

As with bucket policies**,** if you use `aws:PrincipalTags` to create exceptions for principals, consider the scope of your attribute-based access control (ABAC) controls on the tagging of principals.

The following RCP restricts presigned URL usage across all [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) buckets in an organization by limiting signature age to 15 minutes:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyPresignedOver15MinWithExceptions",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": "arn:aws:s3:::*/*",
      "Condition": {
        "NumericGreaterThan": {
          "s3:signatureAge": "900000"
        },
        "StringNotEquals": {
          "aws:PrincipalTag/long-presigned-allowed": "true",
        }
      }
    },
    {
      "Sid": "DenyPresignedOver15MinutesOutsideOrg",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": "arn:aws:s3:::*/*",
      "Condition": {
        "NumericGreaterThan": {
          "s3:signatureAge": "900000"
        },
        "StringNotEquals": {
          "aws:PrincipalOrgID": "${aws:ResourceOrgID}"
        }
      }
    }
  ]
}
```

## Guardrail for s3:authType
<a name="s3-auth-type"></a>

Presigned URLs use [query string authentication](https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-query-string-auth.html), and presigned POSTs use [POST authentication](https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-authentication-HTTPPOST.html). Amazon S3 ([What is Amazon S3?](https://docs.aws.amazon.com/AmazonS3/latest/userguide/)) lets you deny requests based on authentication type by using the [s3:authType](https://docs.aws.amazon.com/AmazonS3/latest/API/bucket-policy-s3-sigv4-conditions.html) condition key. `REST-QUERY-STRING` is the [s3:authType](https://docs.aws.amazon.com/AmazonS3/latest/API/bucket-policy-s3-sigv4-conditions.html) value for query strings, and `POST` is the [s3:authType](https://docs.aws.amazon.com/AmazonS3/latest/API/bucket-policy-s3-sigv4-conditions.html) value for POST.

You can apply the following policy as a service control policy (SCP). The policy uses `s3:authType` to allow only header-based authentication. It also provides a way to make exceptions for individual users or roles.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyNonHeaderAuth",
      "Effect": "Deny",
      "Action": "s3:*",
      "Resource": "*",
      "Condition": {
        "StringNotEquals": {
          "s3:authType": "REST-HEADER",
          "aws:PrincipalTag/non-header-auth-allowed": "true"
        }
      }
    }
  ]
}
```

Denying requests based on authentication type affects any solution or feature that uses the denied authentication type. For example, denying `REST-QUERY-STRING` prevents users from performing uploads or downloads from the Amazon S3 console. If you want users to use the Amazon S3 console, don't use this guardrail, or make an exception for users. On the other hand, if you don't want users to use the Amazon S3 console, you can deny `REST-QUERY-STRING` for users.

If you already deny users direct access to Amazon S3 resources, a guardrail for authentication type might be redundant. However, an `s3:authType` deny statement provides defense-in-depth because implementations that deny direct access usually span many control statements, some with exceptions.

Workload roles typically don't need query string or `POST` authentication. Exceptions are roles that support services designed to use presigned requests. You can create specific exceptions for those roles.

You can also apply a bucket policy to all or selected buckets by using a policy such as the following:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyNonHeaderAuth",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": "arn:aws:s3:::{bucket-name}/*",
      "Condition": {
        "StringNotEquals": {
          "s3:authType": "REST-HEADER",
          "aws:PrincipalTag/non-header-auth-allowed": "true"
        }
      }
    }
  ]
}
```

This bucket policy denies use of the **CopyObject** and **UploadPartCopy** APIs to make cross-Region copies. This policy doesn't affect Amazon S3 Replication because replication doesn't rely on these APIs.

If you want to use a bucket policy such as the preceding policy and still support the cross-Region **CopyObject** or **UploadPartCopy** API, add a condition for `aws:ViaAWSService` similar to the following:

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "DenyNonHeaderAuth",
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": "arn:aws:s3:::{bucket-name}/*",
      "Condition": {
        "StringNotEquals": {
          "s3:authType": "REST-HEADER",
          "aws:PrincipalTag/non-header-auth-allowed": "true"
        },
        "Bool": {
          "aws:ViaAWSService": "false"
        },
      }
    }
  ]
}
```

## Combining presigned guardrails and exceptions to other guardrails
<a name="combining-exceptions"></a>

If you don't plan to apply a guardrail generally to your users and roles, you might want to apply it to the exceptions of other common guardrails, so those exceptions don't support presigned requests.

If you have network restrictions but allow exceptions for external partners or special use cases, block query string or `POST` authentication for those exceptions, unless you specifically require it.

## Limitations to s3:signatureAge
<a name="s3-signature-age-limits"></a>

As an administrator, understand the implications of `s3:signatureAge`. Every signed request includes `X-Amz-Date`, which should indicate the current time. The client and request signer set this value. AWS rejects requests that it considers to have invalid times. However, a signer could generate signatures in advance with a future time. Amazon S3 rejects requests that specify a future time if the signer sends them too far in advance. However, if the signer doesn't send the request until the time that's signed into the signature, the signer could generate the signature earlier and send it later.

`s3:signatureAge` limits the maximum age of `X-Amz-Date` in a signature only for presigned requests. `s3:signatureAge` denies requests that are older than the specified age, even if the expiration in `X-Amz-Expires` or a `POST` policy would have declared them valid. `s3:signatureAge` doesn't change the valid period for requests that don't include an explicit expiration. It also doesn't control the value of `X-Amz-Date` that a client uses for a signature.

If the system clock is wrong or if a client intentionally future-dates requests, the signed time might not be the time the signer generated the signature. This limits how much `s3:signatureAge` can control solutions. A solution that uses the current time when it generates signatures is limited in the expected way: The signatures remain valid for the number of milliseconds that you specify in `s3:signatureAge`. A solution that doesn't use the current time has different limits. One restriction is that the credentials that signed the request must still be valid. As an administrator, you can control the maximum validity of the temporary credentials that you issue. You can allow the credentials to be valid for up to 36 hours or restrict validity to as low as 15 minutes. The expiration of temporary credentials doesn't depend on the value of `X-Amz-Date`.

Long-term credentials don't have this restriction. [Using only temporary credentials](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_identities_unique.html) is a best practice, and you can explicitly revoke any long-term credential, which also invalidates any signatures based on that credential.

Although `s3:signatureAge` is measured in milliseconds, it isn't practical to set it to less than 60 seconds, even if you have a well-synchronized clock and low-latency usage. Settings that are lower than 60 seconds might reject valid requests. If you expect delays between signature generation and request submission, or issues with clock synchronization, account for these when you set `s3:signatureAge`.

## Targeting buckets at scale
<a name="buckets-at-scale"></a>

Service control policies (SCPs) and resource control policies (RCPs) can use `aws:PrincipalTag` to make exceptions for users. You can't use tags on an Amazon S3 bucket to control access through `aws:ResourceTag`―[only object tags are used for access control](https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging-and-policies.html). It isn't generally scalable to add a tag to every object you want to apply this control to.

A solution that fits many use cases is to apply the policy and exception at the account level, either by changing the accounts that the SCP or RCP applies to or by using [aws:ResourceAccount](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourceaccount), [aws:ResourceOrgPaths](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourceorgpaths), or [aws:ResourceOrgID](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourceorgid). For example, an SCP or RCP might be applied to a set of production accounts.

Another solution is to use a [custom AWS Config rule](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules.html) to implement a [detective control](https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-security-controls/detective-controls.html) or [responsive control](https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-security-controls/responsive-controls.html). The goal is for every bucket to contain a bucket policy that includes the required guardrail. In addition to testing the content of a bucket policy, the custom AWS Config rule can retrieve the tags from the bucket and exclude the bucket from the rule if the bucket is tagged with a specific value. If a bucket fails the compliance check, the rule can either mark the bucket as non-compliant or invoke a remediation that adds the guardrail to the bucket's policy.

**Note**
You can't restrict the tag content of requests to [PutBucketTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketTagging.html). To maintain control over how a bucket is tagged, you must limit access to `PutBucketTagging` and [DeleteBucketTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketTagging.html).
