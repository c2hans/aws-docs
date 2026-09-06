---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/presigned-url-best-practices/additional-guardrails.html
---

# Additional guardrails
<a name="additional-guardrails"></a>

When presigned requests are used appropriately by solution builders and users, they provide a secure mechanism for giving users access to data. In addition, the ability to generate presigned requests doesn't provide principals with access that they didn't already have.

In that context, are additional controls necessary? The justification for additional controls isn't based on a need to deny access but to provide the ability to monitor, to approve usage and set boundaries, and to reduce risk from user errors. In this way you can help ensure that usage is appropriate and necessary.

The following guardrails assist you in this goal. Before you enable these controls, you might want to determine existing usage by identifying presigned requests. This identification helps you prepare for the guardrail's impact to existing usage or to plan exceptions where needed.

## Guardrail for s3:signatureAge
<a name="s3-signature-age"></a>

One defining characteristic of presigned requests is that they describe an expiration time. The signature for the request contains a date. This date is transmitted as an `X-Amz-Date` query string parameter for presigned URLs, and as a [Date or x-amz-date header ](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTCommonRequestHeaders.html)for a presigned POST.

Amazon S3 provides a condition key, [s3:signatureAge](https://docs.aws.amazon.com/AmazonS3/latest/API/bucket-policy-s3-sigv4-conditions.html), which you can use to limit the maximum time between the signed date and the effective expiration of the request. This condition can never increase the validity period, but it can reduce it.

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
<a name="exceptions.2aabb4a6-59c0-575b-97c0-0bbe1622fb9e"></a>

If a solution requires a longer time before expiration and is therefore affected by the preceding policy, we recommend that you provide a method to approve exceptions. To avoid enumerating exceptions in an SCP, use [aws:PrincipalTag](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-principaltag), as in the following policy, to manage exceptions in a scalable way. Other AWS examples, such as the [AWS data perimeter policy examples](https://github.com/aws-samples/data-perimeter-policy-examples/blob/main/README.md), use this strategy.

If you implement an exception policy by using `aws:PrincipalTag`, you must control access to setting tags on principals. Tags of this type can come directly from principals and can be controlled by an SCP, as in [this example of controlling which tag values can be set](https://github.com/aws-samples/data-perimeter-policy-examples/blob/main/service_control_policies/data_perimeter_governance_scp.json). A tag of this type can also come from [session tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html), which are set by an identity provider (IdP) or AWS STS. Controlling access to `aws:PrincipalTag` is a complex topic. However, an organization that has experience in using [attribute-based access control (ABAC)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction_attribute-based-access-control.html) will have the experience and controls to enable the appropriate use of `aws:PrincipalTag` for this use case.

In the following example, the `aws:PrincipalTag` condition creates an exception that allows any principal with the named tag (`long-presigned-allowed`) assigned, and set to `true`. With this exception the restriction on signature age is not applied.

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
<a name="bucket-policies.ed04696a-0d2d-5195-8bc5-f44a2c88d4e2"></a>

You can apply bucket policies to all or selected buckets by using a policy as in the following example. Unlike an SCP, a bucket policy also targets [service principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#principal-services) usage. Appendix A doesn't document any expected service principal usage of presigned requests, but if you wanted to implement a control that for the sake of proving that limit, the following policy would provide that control. Also, unlike an SCP, a bucket policy can apply to principals in your management account.

ABAC-based exceptions work in bucket policies in the same way as an SCP. A goal of a bucket policy might be to apply to principals outside the organization, so ABAC exceptions should be constrained to the principals for which ABAC controls apply.

In the following example, the aws:PrincipalTag condition in the first statement creates an exception for a principal with the named tag (`long-presigned-allowed`) assigned, and set to `true`. With this exception the restriction on signature age is not applied. The second statement applies this restriction to all principals outside the AWS organization that owns the bucket. The scope of this second statement should match ABAC controls to set the named tag for principals.

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

You can apply a policy to buckets at scale by using [resource control policies (RCPs)](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html). Like SCPs and unlike bucket policies, RCPs do not target service principal usage. RCPs affect non-service principals from any account, but they do not affect resources in the management account. For more information, see the [AWS Organizations documentation.](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_rcps.html#actions-not-restricted-by-rcps)

As with bucket policies**,** if you use `aws:PrincipalTags` to create exceptions for principals, keep in mind the scope of ABAC controls on the tagging of principals.

The following RCP restricts presigned URL usage across all S3 buckets in an organization by limiting signature age to 15 minutes:

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

Presigned URLs use [query string authentication](https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-query-string-auth.html), and presigned POSTs always use [POST authentication](https://docs.aws.amazon.com/AmazonS3/latest/API/sigv4-authentication-HTTPPOST.html). Amazon S3 supports the denial of requests based on authentication type through the [s3:authType](https://docs.aws.amazon.com/AmazonS3/latest/API/bucket-policy-s3-sigv4-conditions.html) condition key. `REST-QUERY-STRING` is the [s3:authType](https://docs.aws.amazon.com/AmazonS3/latest/API/bucket-policy-s3-sigv4-conditions.html) value for query strings, and `POST` is the [s3:authType](https://docs.aws.amazon.com/AmazonS3/latest/API/bucket-policy-s3-sigv4-conditions.html) value for POST.

You can apply the following policy as an SCP. The policy uses `s3:authType` to allow only header-based authentication. It also configures a method to provide exceptions to individual users or roles.

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

Perhaps you already deny users direct access to Amazon S3 resources. In this case, a guardrail for authentication type is redundant. However, an `s3:authType` deny statement provides defense-in-depth utility because implementations to deny direct access usually span many control statements, some with exceptions.

Roles that are used for workloads won't typically need access to query string or `POST` authentication. Exceptions are roles that support services designed to use presigned requests. You can create specific exceptions for those roles.

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

This bucket policy has the effect of denying the use of the **CopyObject** and **UploadPartCopy** APIs to make cross-Region copies. Amazon S3 Replication isn't affected because it doesn't rely on these APIs.

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

If you have network restrictions but allow exceptions for external partners or special use cases, you should block query string or `POST` authentication when those exceptions are applied, unless they're specifically identified as being required.

## Limitations to s3:signatureAge
<a name="s3-signature-age-limits"></a>

Administrators will find it useful to understand the implications of `s3:signatureAge` more fully. Every signed request includes `X-Amz-Date`, which should indicate the current time. This value is filled by the client and request signer. AWS rejects requests that it considers to have invalid times. However, a signer could generate signatures in advance with a future time. Amazon S3 rejects requests that specifies a future time if it's sent too far in advance. However, if the request isn't sent until the time that's signed into the signature, the signature could be generated earlier and sent later.

`s3:signatureAge` limits the maximum age of `X-Amz-Date` in a signature only for presigned requests. Requests that are older than the specified age are denied, even if the expiration in `X-Amz-Expires` or a `POST` policy would have declared it valid. `s3:signatureAge` doesn't change the valid period for requests that don't include an explicit expiration. It also doesn't control the value of `X-Amz-Date` that a client uses for a signature.

If the system clock is wrong or if a client intentionally future-dates requests, the signed time might not be the time the signature was generated. This limits how much `s3:signatureAge` can control solutions. A solution that uses the current time when it generates signatures is limited in the expected way: The signatures remain valid for the number of milliseconds specified in `s3:signatureAge`. A solution that doesn't use the current time will have different limits. One restriction is that the credentials that were used to sign the signature must still be valid. As an administrator, you can control the maximum validity of temporary credentials issued. You can allow the credentials to be valid for up to 36 hours or restrict validity to as low as 15 minutes. The expiration of temporary credentials isn't dependent on the value of `X-Amz-Date`.

Permanent credentials don't have this restriction. [Using only temporary credentials](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/sec_identities_unique.html) is a best practice, and you can explicitly revoke any permanent credential, which would also invalidate any signatures based upon that credential.

Although `s3:signatureAge` is measured in milliseconds, it isn't practical to set it to less than 60 seconds, even if you have a well-synchronized clock and low-latency usage. Settings that are lower than 60 seconds carry the risk of rejecting valid requests. If you expect delays between signature generation and request submission, or issues with clock synchronization, you should account for these in your management of `s3:signatureAge`.

## Targeting buckets at scale
<a name="buckets-at-scale"></a>

SCPs and RCPs can use `aws:PrincipalTag` to make exceptions for users. You can't use tags on a bucket to control access through `aws:ResourceTag`―[only object tags are used for access control](https://docs.aws.amazon.com/AmazonS3/latest/userguide/tagging-and-policies.html). It isn't generally scalable to add a tag to every object you want to apply this control to.

A solution that fits many use cases is to apply the policy and exception at the account level, either by changing the accounts that the SCP or RCP applies to or by using [aws:ResourceAccount](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourceaccount), [aws:ResourceOrgPaths](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourceorgpaths), or [aws:ResourceOrgID](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_condition-keys.html#condition-keys-resourceorgid). For example, an SCP or RCP might be applied to a set of production accounts.

Another solution is to use a [custom AWS Config rule](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules.html) to implement a [detective control](https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-security-controls/detective-controls.html) or [responsive control](https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-security-controls/responsive-controls.html). The goal would be for every bucket to contain a bucket policy with the appropriate guardrail. In addition to testing the content of a bucket policy, the custom AWS Config rule can retrieve the tags from the bucket and exclude the bucket from the rule if the bucket is tagged with a specific value. If that rule fails its compliance check, it could either mark the bucket as non-compliant or invoke a remediation to add the guardrail to the bucket's policy.

**Note**
You can't restrict the tag content of requests to [PutBucketTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutBucketTagging.html). To maintain control over how a bucket is tagged, you must limit access to `PutBucketTagging` and [DeleteBucketTagging](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucketTagging.html).
