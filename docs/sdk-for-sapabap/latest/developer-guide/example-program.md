---
source_url: https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/example-program.html
---

# Amazon S3 example program
<a name="example-program"></a>

This section walks you through a simple example program to list the contents of an Amazon S3 bucket by calling `ListObjectsV2`.

**Topics**
+ [Prerequisites](#prerequisites-example-program)
+ [Code](#code-example-program)
+ [Code sections](#code-sections)

## Prerequisites
<a name="prerequisites-example-program"></a>

You must meet the following prerequisites to run this example program.
+ You have an Amazon S3 bucket. In this tutorial, the bucket is named `demo-invoices.customer.com`.
+ Transaction `/AWS1/IMG`:
  + Has a defined SDK profile named `DEMO_S3`.
    + In the SDK profile, the logical IAM role `TESTUSER` must map to an IAM role, such as `arn:aws:iam::{{111122223333}}:role/SapDemoFinance` which grants `s3:ListBucket` permission to list the contents of your Amazon S3 bucket.
  + Has a logical resource named `DEMO_BUCKET` that is mapped to your Amazon S3 bucket with the SID and client of your SAP system.
+ Your user has a PFCG role that:
  + Authorizes the user to access `DEMO_S3` SDK profile via auth object - `/AWS1/SESS`.
  + Authorizes the user for logical IAM role `TESTUSER` access via auth object - `/AWS1/LROL`.
+ Your SAP system can authenticate itself to AWS using the method defined in the SDK profile.
+ Your Amazon EC2 instance profile grants your SAP system the rights to `sts:assumeRole` in the IAM role `arn:aws:iam::{{111122223333}}:role/SapDemoFinance` mapped in the SDK profile.

## Code
<a name="code-example-program"></a>

The following code block demonstrates what your code would look like.

```
REPORT  zdemo_s3_listbuckets.

START-OF-SELECTION.
  PARAMETERS pv_lres TYPE  /aws1/rt_resource_logical
                     DEFAULT 'DEMO_BUCKET' OBLIGATORY.

  DATA(go_session) = /aws1/cl_rt_session_aws=>create( 'DEMO_S3'  ).
  DATA(gv_bucket)   = go_session->resolve_lresource( pv_lres ).

  DATA(go_s3)       = /aws1/cl_s3_factory=>create( go_session ).

  TRY.
      DATA(lo_output) = go_s3->listobjectsv2(
            iv_bucket = CONV string( gv_bucket )
            iv_maxkeys = 100
      ).
      LOOP AT lo_output->get_contents(  ) INTO DATA(lo_object).
        DATA lv_mdate TYPE datum.
        CONVERT TIME STAMP lo_object->get_lastmodified( )
                TIME ZONE 'UTC'
                INTO DATE lv_mdate.
        WRITE: /  CONV text30( lo_object->get_key( ) ),
                 lv_mdate, lo_object->get_size( ).
      ENDLOOP.
    CATCH /aws1/cx_rt_generic INTO DATA(lo_ex).
      DATA(lv_msg) = lo_ex->if_message~get_text(  ).
      MESSAGE lv_msg TYPE 'I'.
  ENDTRY.
```

## Code sections
<a name="code-sections"></a>

The following is a review of the code in sections.

```
  PARAMETERS pv_lres TYPE  /aws1/rt_resource_logical
                     DEFAULT 'DEMO_BUCKET' OBLIGATORY.
```

The user can't specify a physical bucket name. They specify a logical bucket and the system administrators (specifically the business analyst) in coordination with the AWS administrator map logical buckets to physical buckets in `/AWS1/IMG`. In most business scenarios, the user doesn't have a chance to choose the logical bucket — the logical resource ID is hard coded in the code or configured in a custom configuration table.

```
  DATA(go_session) = /aws1/cl_rt_session_aws=>create( 'DEMO_S3'  ).
```

This line establishes a security session and declares that this ABAP program expects to use the `DEMO_S3` SDK profile. This call is the connection to the SDK configuration and pulls in the default Region, authentication settings, and the desired IAM Role. A call to `AUTHORIZATION-CHECK` is automatically made to ensure that authorization object `/AWS1/SESS` is satisfied. Additionally, `AUTHORIZATION-CHECK` calls will be made to determine the most powerful (lower sequence number) logical IAM role the user is authorized for, based on the authorization object `/AWS1/LROL`. The SDK will assume that the IAM role is mapped to the logical IAM role for the SID and client. Then, the session object activates tracing based on the trace settings in the `IMG`.

If the user is not authorized for the requested SDK profile or for any available logical IAM role, an exception will be raised.

```
DATA(gv_bucket)   = go_session->resolve_lresource( pv_lres ).
```

This line resolves the logical resource to a physical bucket name. If the logical resource cannot be resolved because the configuration has no mapping for this SID/client combination, an exception will be raised.

```
  DATA(go_s3)       = /aws1/cl_s3_factory=>create( go_session ).
```

This line creates an API object for Amazon S3 using the `create()` method of `/aws1/cl_s3_factory`. The returned object is of type `/aws1/if_s3` which is the interface for an Amazon S3 API. A separate API object must be created for each service. For example, if an ABAP program is consuming Amazon S3, AWS Lambda, and DynamoDB, then it creates API objects from `/aws1/cl_s3_factory`, `/aws1/cl_lmd_factory`, and `/aws1/cl_dyn_factory`.

There are some optional parameters to the constructor which enable you to specify the Region if you want to override the default Region configured `IMG`. In this way, there can be two instances of `/aws1/if_s3`, one for `us-east-1` and one for `us-west-2`, if you want to copy objects from a bucket in one Region to a bucket in another Region. Similarly, you can create two different security session objects and use them to create two separate instances of `/aws1/cl_s3`, if you need a report to read from a finance-related bucket and write objects to a logistics-related bucket.

```
      DATA(lo_output) = go_s3->listobjectsv2(
            iv_bucket = CONV string( gv_bucket )
            iv_maxkeys = 100
      ).
```

 This line is a call to `ListObjectsV2`. It requires simple input arguments and returns a single object. These objects may represent deep JSON and XML data, de-serialized into an ABAP object-oriented construct. It can be quite complicated in some cases. Now, you only need to process the output to list the contents of the bucket.

```
      LOOP AT lo_output->get_contents(  ) INTO DATA(lo_object).
        DATA lv_mdate TYPE datum.
        CONVERT TIME STAMP lo_object->get_lastmodified( )
                TIME ZONE 'UTC'
                INTO DATE lv_mdate.
        WRITE: /  CONV text30( lo_object->get_key( ) ),
                 lv_mdate, lo_object->get_size( ).
      ENDLOOP.
```

The data is accessed using a `GET...()` style method that hides the internal representation of the data. `GET_CONTENTS( )` returns an ABAP table and each row itself contains an object representing a single Amazon S3 entry. In most cases, AWS SDK takes this object-oriented approach and all data is represented as objects and tables. The `LastModified` field is represented as a timestamp that can be converted to a date with the ABAP-native `CONVERT TIME STAMP` command. the `GET_SIZE()` returns an `INT4` for easy math and formatting operations.

```
    CATCH /aws1/cx_rt_generic INTO DATA(lo_ex).
      DATA(lv_msg) = lo_ex->if_message~get_text(  ).
      MESSAGE lv_msg TYPE 'I'.
```

All errors – connection, 4xx client, 5xx server, or any ABAP error, such as authorization or configuration errors, are represented as exceptions. You can tackle each exception separately. You have the choice of whether an exception should be handled as an informational error, a retry, warning, short dump, or any other kind of handling.
