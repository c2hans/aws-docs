---
source_url: https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/features.html
---

# AWS SDK for SAP ABAP features
<a name="features"></a>

AWS SDK for SAP ABAP provides the following features.

**Topics**
+ [Programmatic configuration](#programmatic-configuration)
+ [Waiters](#waiters)
+ [Paginators](#paginators)
+ [Retry behavior](#retry-behavior)
+ [Presigners](#presigners)
+ [Cross-account IAM role chaining](#source-profile)

## Programmatic configuration
<a name="programmatic-configuration"></a>

Use `/n/AWS1/IMG` IMG transacation for AWS SDK for SAP ABAP, and Custom Business Configuration application for AWS SDK for SAP ABAP - BTP edition for programmatic configuration.

To begin programmatic configuration, begin by retrieving a configuration object with the `get_config( )` command.

```
data(lo_config) = lo_s3->get_config( ).
```

Each configuration object implements `/AWS1/IF_RT_CONFIG` interface that includes `GET`ters and `SET`ters corresponding to the `IMG`. For example, the default region can be overridden. See the following example command.

```
lo_s3->get_config( )->/aws1/if_rt_config~set_region( 'us-east-1' ).
```

Some configuration objects have no `IMG` representation and can only be set programmatically, such as maximum retry attempts. See the following example command.

```
lo_s3->get_config( )->/aws1/if_rt_config~set_max_attempts( 10 ).
```

The configuration object of AWS services can also include service specific methods that are not represented in `/aws1/if_rt_config`. For example, Amazon S3 can address a bucket named `foobucket` using either `foobucket.s3.region.amazonaws.com` virtual endpoint or `s3.region.amazonaws.com/foobucket` path style. You can enforce the use of path style with the following example command.

```
lo_s3->get_config( )->set_forcepathstyle( abap_true ).
```

For more information about service configurations, see [AWS SDK for SAP ABAP – API Reference Guide](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html).

## Waiters
<a name="waiters"></a>

When working with asynchronous AWS APIs, you need to wait for a certain resource to become available before taking further actions. For example, the `CREATETABLE()` API of Amazon DynamoDB responds right away with table status `CREATING`. You can initiate read or write operations only after the status of the table has changed to `ACTIVE`. Waiters give you the ability to confirm that AWS resources are in a particular state before performing actions on them.

Waiters use service operations to poll the status of AWS resources until the resource reaches the intended state or until it is determined that the resource doesn't reach the desired state. It can be time-consuming and error-prone to write the code to poll AWS resources continually. Waiters help in simplifying this complexity by taking the responsibility of performing polls on your behalf.

See the following Amazon S3 example using waiter.

```
DATA(lo_session) = /aws1/cl_rt_session_aws=>create( cv_pfl ).
DATA(lo_s3) = /aws1/cl_s3_factory=>create( lo_session ).

" Create a bucket - initiates the process of creating an S3 bucket and might return before the bucket exists
lo_s3→createbucket( iv_bucket = |amzn-s3-demo-bucket| ).

" Wait until the newly created bucket becomes available
lo_s3->get_waiter( )->bucketexists(
    iv_max_wait_time = 200
    iv_bucket = |amzn-s3-demo-bucket|
).
```
+ In this example, Amazon S3 client is used to create a bucket. The `get_waiter()` command is implemented to specify when the `bucketexists`.
+ You must specify the `iv_max_wait_time` parameter for each waiter. It represents the total amount of time a waiter must wait before completion. In the preceding example, a waiter can run for 200 seconds.
+ You may need to provide additional inputs for required parameters. In the preceding example, Amazon S3 bucket name is required for `iv_bucket` parameter.
+ `/AWS1/CX_RT_WAITER_FAILURE` exception indicates that the waiter exceeded the maximum time specified in `iv_max_wait_time` parameter.
+ `/AWS1/CX_RT_WAITER_TIMEOUT` exception indicates that the waiter has stopped due to not reaching the desired state.

## Paginators
<a name="paginators"></a>

Some AWS service operations offer paged responses. They are paginated to return a fixed amount of data with each response. You need to make subsequent requests with a token or a marker to retrieve the entire set of results. For instance, the `ListObjectsV2` Amazon S3 operation return up to 1,000 objects at a time. You must make subsequent requests with the appropriate token to get the next page of results.

Pagination is the process of sending successive requests to pick up where a previous request left off. Paginators are iterators of results provided by SDK for SAP ABAP. You can use paginated APIs with ease, and without understanding the underlying mechanism of API using pagination tokens.

**Working with paginators**

You can create paginators with the `get_paginator()` method that returns a paginator object. The paginator object calls the operation being paginated. The paginator object accepts required parameters to be provided to the underlying API. This process returns an iterator object that can be used to iterate over paginated results, using the `has_next()` and `get_next()` methods.
+ `has_next()` returns a boolean value indicating if there are more responses or pages available for the called operation.
+ `get_next()` returns the operation response.

The following example list all objects in an S3 bucket retrieved by using paginator.

```
DATA(lo_session) = /aws1/cl_rt_session_aws=>create( 'DEMO' ).
DATA(lo_s3) = /aws1/cl_s3_factory=>create( lo_session ).

TRY.
    DATA(lo_paginator) = lo_s3->get_paginator( ).
    DATA(lo_iterator) = lo_paginator->listobjectsv2(
        iv_bucket = 'example_bucket'
    ).
    WHILE lo_iterator->has_next( ).
        DATA(lo_output) = lo_iterator->get_next( ).
        LOOP AT lo_output->get_contents(  ) INTO DATA(lo_object).
            WRITE: / lo_object->get_key( ), lo_object->get_size( ).
        ENDLOOP.
    ENDWHILE.
CATCH /aws1/cx_rt_generic INTO DATA(lo_ex).
    MESSAGE lo_ex->if_message~get_text(  ) TYPE 'I'.
ENDTRY.
```

## Retry behavior
<a name="retry-behavior"></a>

SDK for SAP ABAP enables you to configure the maximum number of retries for requests to AWS services that fail due to throttling or transient errors. The number of retries allowed at the service client level, that is the number of times the SDK retries the operation before failing and raising an exception is specified by the `AV_MAX_ATTEMPTS` attribute in the service configuration object. When a service client object is created, the SDK configures `AV_MAX_ATTEMPTS` attribute to a default value of 3. The service configuration object may be used to programmatically set the maximum retry attempt to a desired value. See the following example for more details.

```
" Retrieve configuration object using Amazon S3 service’s get_config( ) method
DATA(lo_config) = lo_s3->get_config( ).

" Set the maximum number of retries to 5
lo_config->/aws1/if_rt_config~set_max_attempts( 5 ).

" Get the value of the maximum retry attempt.
DATA(lv_max_retry_attempts) = lo_config->/aws1/if_rt_config~get_max_attempts( ).
```

**Note**
Although the configuration object ABAP SDK allows *retry mode* to be set with the `/AWS1/IF_RT_CONFIG~SET_RETRY_MODE()` method, the SDK only supports the `standard` retry mode. For more information, see [Retry behavior](https://docs.aws.amazon.com/sdkref/latest/guide/feature-retry-behavior.html) in AWS SDKs and Tools Reference Guide.

## Presigners
<a name="presigners"></a>

You can use presigned URLs to grant time-limited access to some AWS services. A presigned URL can be entered in a browser or used by a program to perform the service operation. You can use the presigned URL multiple times, up to the expiration date and time. For more information, see [ Working with presigned URLs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-presigned-url.html) SDK for SAP ABAP clients for services that support presigners will have a special method called `GET_PRESIGNER()` to create a presigner for that service. Then call a method of the presigner, which correspond to the methods of the API client, except they return a presigned URL instead of actually performing the operation.

```
" Retrieve a presigner for Amazon S3
DATA(lo_presigner) = lo_s3->get_presigner( iv_expires_sec = 600 ).

" the presigner getobject() method has the same signature as
" lo_s3->getobject(), but it doesn't actually make the call.
" to the service.  It just prepares a presigned URL for a future call
DATA(lo_presigned_req) = lo_presigner->getobject( iv_bucket = iv_bucket_name iv_key = iv_key ).

" You can provide this URL to a web page, user, email etc so they
" can retrieve the file.  The URL will expire in 10 minutes.
ov_url = lo_presigned_req->get_url( ).
```

## Cross-account IAM role chaining
<a name="source-profile"></a>

Cross-account IAM role chaining support enables seamless access to resources across multiple AWS accounts through source profile configuration. This feature allows you to configure multiple role assumptions, where one profile assumes a role that then assumes another role, enabling complex cross-account access patterns.

For more information, see [Using Source Profile for Cross-Account Access](https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/source-profile.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for SAP ABAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-sapabap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
