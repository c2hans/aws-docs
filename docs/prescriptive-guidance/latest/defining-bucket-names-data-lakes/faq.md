---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/defining-bucket-names-data-lakes/faq.html
---

# FAQ
<a name="faq"></a>

This section provides answers to commonly raised questions about defining Amazon Simple Storage Service (Amazon S3) bucket and path names for data lake layers on the AWS Cloud.

## What name should I use for a multi-Region bucket?
<a name="q1"></a>

You can use our recommended Amazon S3 bucket naming format and change the AWS Region identifier. Examples include `examplecompany-raw-useast1-12345-dev` and `examplecoompany-raw-uswest1-12345-dev`.

## Do I need to use raw, stage, and analytics as the names for my data lake layers?
<a name="q2"></a>

No, you can name your layers according to your requirements. However, we strongly recommended that you use an Amazon S3 bucket for the data layer that contains the original file formats and enable versioning for this bucket.

## Is it possible to rename an Amazon S3 bucket?
<a name="q3"></a>

No. If you want to use a different Amazon S3 bucket name, you must create a new bucket with the new name. This is one reason why we recommend having a clearly defined and consistent naming approach for Amazon S3 buckets.

## What happens if I delete a bucket and want to reuse the name?
<a name="q4"></a>

If you delete an Amazon S3 bucket and want to create a new bucket with the same name, you must wait for the name to become available again. It can take 48–72 hours for the changes to take effect. It's a best practice to wait at least 48 hours before creating a new bucket that reuses a previous name. Amazon S3 bucket names are globally unique, and all AWS accounts share the same namespace.

## Are there limitations on what I can include in my bucket name or path name?
<a name="q5"></a>

Only lowercase letters, numbers, dashes, and dots are allowed in Amazon S3 bucket names. Bucket names must be 3–63 characters in length, must begin and end with a number or letter, and cannot be in an IP address format. The names must also be globally unique.

For Amazon S3 bucket paths, you can use uppercase letters, but we recommend that you only use lowercase letters. Paths can also include additional symbols, but we recommend that you use only underscores, dashes, slashes, and numbers.

## Can I use more layers than the landing zone, raw, stage, and analytics layers in my data lake?
<a name="q6"></a>

Yes, you can use as many layers as you want. However, we recommend having a landing zone and raw layer for your raw data, an intermediate layer for formatted data, and a layer for highly-modeled data.

## What happens if I have not defined my parameters?
<a name="q7"></a>

Certain parameters, such as business units, don't need to be incorporated into the Amazon S3 bucket name but can be part of the path. This means that they don't need to be immediately determined because paths can be added after an Amazon S3 bucket is created.

## How can I track costs at the business unit level?
<a name="q8"></a>

This depends on your account strategy. If your business units have separate AWS accounts, you can assign cost allocation tags to Amazon S3 buckets that reflect the bucket costs for each business unit.

If your account strategy doesn't separate business units into different AWS accounts, then you can use different buckets for each business unit. Add the business unit to the bucket name, such as `exampleco-businessunit1-raw-useast1-12345-dev`. However, this means that you have to manage many Amazon S3 buckets.

## What features should I consider when creating a naming standard?
<a name="q9"></a>

You must make sure that your Amazon S3 bucket names use features that are only available at the bucket level. For example, cost tags, bucket encryption, and versioning are features that are only available for an entire Amazon S3 bucket. This means that they apply to all objects and paths in the bucket.

Object versioning is also an important feature to consider. You should turn on versioning for your raw layer's Amazon S3 buckets. This makes sure that you can access previous versions if there are changes to the data. However, versioning might not be necessary for all the layers in your data lake, and retaining multiple versions can cause unnecessary costs.
