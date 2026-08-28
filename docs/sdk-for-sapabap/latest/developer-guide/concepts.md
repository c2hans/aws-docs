---
source_url: https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/concepts.html
---

# SDK for SAP ABAP concepts
<a name="concepts"></a>

This section covers the basic concepts of AWS SDK for SAP ABAP.

**Topics**
+ [API classes](#api-classes)
+ [Additional objects](#additional-objects)
+ [Structure classes](#structure-classes)
+ [Arrays](#arrays)
+ [Maps](#maps)
+ [Higher level functions](#higher-level-functions)

## API classes
<a name="api-classes"></a>

Each AWS service is assigned a three-letter acronym or `TLA`. The service is represented by an interface in the `/AWS1/IF_<TLA>` format. We will call this the service interface. The API class is in the `/AWS1/API_<TLA>` package. The service interface consists of one method for each AWS operation (we will call these methods Operation Methods). To see a complete module list of AWS SDK for SAP ABAP TLAs, see [AWS SDK for SAP ABAP - Module List](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/tla.html).

Each operation method has some `IMPORTING` arguments and at the most one `RETURNING` argument. Often, these arguments will be objects with complicated constructors and a long set of `GET…()` methods. In many cases, the objects will contain nested objects, recursive references, tables of objects, tables of tables, and so forth. This is because AWS services are passing deep XML and JSON structures, which cannot be represented by a flat set of arguments.

The `RETURNING` argument is always a class, even if the class contains only a single attribute.

## Additional objects
<a name="additional-objects"></a>

In addition to containing the primary API class, each API package contains various related repository and data dictionary objects.
+ A class for each structure-type object.
+ A class for any primitive data type which appears in a table. For example, if a service returns a table of strings, the ABAP API will represent it as a table of objects, where each object is a wrapper class that encapsulates a string. This is so that the wrapper class can hide the details of representing a null string that cannot be represented natively in ABAP.
+ An exception class for any specific errors defined by the service.
+ Data elements for each primitive data type. Each data type has its own data element in order to be self-documenting.
+ Additional objects for internal processing, such as XSLT transforms for serializing and de-serializing XML and JSON payloads.

## Structure classes
<a name="structure-classes"></a>

Most AWS data, sent and received by the service, is represented by AWS SDK as classes. These classes represent structures of data and hide the internal details of the storage. In particular, the classes hide the way the SDK represents *this field has no value*.

 For each field in a structure class, there are three methods.

 **`GET_field( )`**

The `GET_field( )` method
+ Returns the value of the field, or
+ If the field has no value, it returns a default value, which you can set as an optional parameter.

For example, consider the following code that prints the location constraint of a bucket.

```
DATA(lo_location) = go_s3->getbucketlocation( iv_bucket = CONV string( gv_bucket ) ).
WRITE: / 'Bucket Location: ',
   lo_location->get_locationconstraint( ).
```

If the bucket has no location constraint at all (as in the case of `us-east-1`), then `GET_LOCATIONCONSTRAINT( )` will return the empty string. You can override this behavior and specify the desired value if the field has no value at all.

```
DATA(lo_location) = go_s3->getbucketlocation( iv_bucket = CONV string( gv_bucket ) ).
WRITE: / 'Bucket Location: ',
   lo_location->get_locationconstraint( iv_value_if_missing = 'assuming us-east-1' ).
```

Now the program will write `Bucket Location: assuming us-east-1` if `getbucketlocation()`‘s result does not return a location.

It is possible to ask the GET( ) method to return a specific result if the requested value is completely missing, see the following code example.

```
data(lo_location) = go_s3->GETBUCKETLOCATION(
   new /AWS1/CL_S3_GET_BUCKET_LOC_REQ( iv_bucket = gv_bucket )
).
write: / 'Location constraint: ',
         lo_location->GET_LOCATIONCONSTRAINT( 'NopeNopeNope'  ).
```

In this case, if there is no location constraint, `GET_LOCATIONCONSTRAINT( )` will return `NopeNopeNope`.

 **`HAS_field( )`**

`HAS_field( )` method is a way to find out if the field has a value or not. See the following example.

```
if NOT lo_location->HAS_LOCATIONCONSTRAINT( ).
   write: / 'There is no location constraint'.
endif.
```

If a certain field is known to always have a value, there will be no `HAS_field( )` method.

 **`ASK_field( )`**

The `ASK_field( )` method returns the value of the field or raises an exception if it has no value. This is a convenient way to process a number of fields, and bail out of the logic and take a different approach if any of the fields have no value.

```
TRY.
    WRITE: / 'Location constraint: ', lo_location->ask_locationconstraint( ).
CATCH /aws1/cx_rt_value_missing.
    WRITE: / 'Never mind, there is no location  constraint'.
ENDTRY.
```

Note that `/AWS1/CX_RT_VALUE_MISSING` is a static exception and you will get a warning if you choose not to catch it.

 **Best practices**

In general, you can use the `GET_field( )` method as it treats a null string as an empty string and is the most ABAP-like of the three options. However, it does not let you easily distinguish between situations where the field has a blank value and where the field has no value. If your business logic depends on distinguishing missing data versus blank data, then the `HAS` or `ASK` methods let you handle these cases.

## Arrays
<a name="arrays"></a>

Arrays are represented as ABAP standard tables of objects.

A JSON array can contain null values, such as the following array: `[‘cat’, ‘dog’, null, ‘horse’]`. This is referred to as a sparse array. It is represented in ABAP as an internal table of object references, and the `null` value is represented in the table as a true ABAP `null` value. When iterating through a sparse table, you must check for `null` values to avoid accessing a `null` object and getting a `CX_SY_REF_IS_INITIAL`exception. In practice, sparse arrays are rare in AWS services.

To initialize an array of objects, it is convenient to use the new ABAP 7.40 constructs. Consider this launch of an Amazon EC2 instance with several security groups assigned:

```
ao_ec2->runinstances(
    iv_imageid                   = lo_latest_ami->get_imageid( )
    iv_instancetype              = 't2.micro'
    iv_maxcount                  = 1
    iv_mincount                  = 1
    it_securitygroupids          = VALUE /aws1/cl_ec2secgrpidstrlist_w=>tt_securitygroupidstringlist(
                                    ( NEW /aws1/cl_ec2secgrpidstrlist_w( 'sg-12345678' ) )
                                    ( NEW /aws1/cl_ec2secgrpidstrlist_w( 'sg-55555555' ) )
                                    ( NEW /aws1/cl_ec2secgrpidstrlist_w( 'sg-99999999' ) )
                                )
    iv_subnetid                  = ao_snet->get_subnetid( )
    it_tagspecifications         = make_tag_spec( 'instance' )
)
```

## Maps
<a name="maps"></a>

JSON maps are represented in ABAP as `Hashed Tables` where each table row has only two components.
+  `KEY` – a string which is the `UNIQUE KEY` of the table.
+  `VALUE` – an object containing the value.

A map is one of the very few cases where AWS SDK uses a true structure, rather than a class. This is necessary because ABAP hashed tables cannot have an object reference as the key field, and AWS map keys are always non-null strings.

## Higher level functions
<a name="higher-level-functions"></a>

The [API classes](#api-classes) described in the preceding section precisely mirror the AWS service APIs and represent those APIs as familiar ABAP classes. In some cases, the SDK also includes higher level functions that build on top of the API classes to simplify certain operations. The higher level functions are included for programmer convenience and do not replace the lower-level API classes.

If the SDK includes higher level functions for a module, they are included in the same transport and can be access through a factory class called `/AWS1/CL_TLA_L2_FACTORY`. The factory class includes methods to create various higher level clients for the module that are documented along with the rest of the API with the [API documentation](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for SAP ABAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-sapabap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
