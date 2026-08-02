---
source_url: https://docs.aws.amazon.com/location/previous/developerguide/database-address-validation.html
---

# Amazon Aurora PostgreSQL user-defined functions for Amazon Location Service
<a name="database-address-validation"></a>

You can use Amazon Location Service to work with coordinates and addresses stored in database tables to clean and enrich your geospatial data.

For example:
+ You can use geocoding to convert addresses to coordinates to normalize and fill gaps in data for addresses stored in a database table.
+ You can geocode addresses to obtain their positions and use the coordinates with database spatial functions, such as a function that shows rows in a specified area.
+ You can use enriched data to generate automated reporting, such as generating an automated report that illustrates all devices in a given area, or an automated report for machine learning that illustrates areas with higher failure rates when sending location updates.

This tutorial shows how to format and enrich addresses stored in an Amazon Aurora PostgreSQL database table using Amazon Location Service.
+ **Amazon Aurora PostgreSQL** – A fully managed relational database engine, compatible with MySQL and PostgreSQL, that outputs up to five times the throughput of MySQL and up to three times the throughput of PostgreSQL without changing most of your existing application. For more information, see [What is Amazon Aurora?](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/CHAP_AuroraOverview.html) in the *Amazon Aurora User Guide*.

**Important**
The resulting application in this tutorial uses a place index that stores geocoding results. For information about applicable charges for storing geocoding results, see [Amazon Location Service pricing](https://aws.amazon.com/location/pricing/).

Sample code is available in the Amazon Location Service samples repository on [GitHub](https://github.com/aws-samples/amazon-location-samples/tree/main/aurora-udfs), which includes [an AWS CloudFormation template](https://github.com/aws-samples/amazon-location-samples/tree/main/aurora-udfs/cloudformation/template.yaml).

**Topics**
+ [Overview](#aurora-amazon-location-overview)
+ [Prerequisites](#aurora-amazon-location-prerequisites)
+ [Quick start](#aurora-amazon-location-quick-start)
+ [Create a place index resource](#aurora-create-place-index)
+ [Create an AWS Lambda function for geocoding](#aurora-create-lambda)
+ [Grant Amazon Aurora PostgreSQL access to AWS Lambda](#aurora-invoke-API)
+ [Invoke the AWS Lambda function](#aurora-setup-table)
+ [Enriching a database containing address data](#aurora-run-sql)
+ [Next steps](#aurora-amazon-location-next-steps)

## Overview
<a name="aurora-amazon-location-overview"></a>

![Architecture diagram showing Amazon Aurora exchanging positions with Lambda and Location Service.](http://docs.aws.amazon.com/location/previous/developerguide/images/aurora_architecture.PNG)

The architecture involves the following integrations:
+  This solution uses an Amazon Location place index resource to support geocoding queries using the operation `SearchPlaceIndexForText`.
+ AWS Lambda uses a Python Lambda that geocodes addresses when an IAM policy gives permission to allow AWS Lambda to call the Amazon Location geocoding operation, `SearchPlaceIndexForText`.
+ Grant permission to Amazon Aurora PostgreSQL to invoke the geocoding Lambda function using an SQL user-defined function.

## Prerequisites
<a name="aurora-amazon-location-prerequisites"></a>

Before you begin, you need the following prerequisites:
+ An Amazon Aurora PostgreSQL cluster. For more information about [Creating an Amazon Aurora DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/Aurora.CreateInstance.html), see the *Amazon Aurora User Guide*.
**Note**
If your Amazon Aurora cluster isn't publicly available, you must also configure Amazon Aurora to connect to AWS Lambda in a virtual private cloud (VPC) in your AWS account. For more information, see [Grant Amazon Aurora PostgreSQL access to AWS Lambda](#aurora-invoke-API).
+ An SQL developer tool to connect to the Amazon Aurora PostgreSQL cluster.

## Quick start
<a name="aurora-amazon-location-quick-start"></a>

As an alternative to going through the steps in this tutorial, you can launch a quick stack to deploy an AWS Lambda function supporting the Amazon Location operation `[SearchPlaceIndexForText](https://docs.aws.amazon.com/location-places/latest/APIReference/API_SearchPlaceIndexForText.html)`. This automatically configures your AWS account to allow Amazon Aurora to call AWS Lambda.

Once you configure your AWS account, you will need to:
+ Add the Lambda feature to Amazon Aurora. See Add the IAM role to a Amazon Aurora DB cluster in [Grant Amazon Aurora PostgreSQL access to AWS Lambda](#aurora-invoke-API).
+ Load the user-defined function into your database. See [Invoke the AWS Lambda function](#aurora-setup-table).

[https://console.aws.amazon.com/cloudformation/home#/stacks/quickcreate?templateUrl=https%3A%2F%2Famazon-location-cloudformation-templates.s3.us-west-2.amazonaws.com%2Faurora-udfs%2Ftemplate.yaml&stackName=AuroraUDFs](https://console.aws.amazon.com/cloudformation/home#/stacks/quickcreate?templateUrl=https%3A%2F%2Famazon-location-cloudformation-templates.s3.us-west-2.amazonaws.com%2Faurora-udfs%2Ftemplate.yaml&stackName=AuroraUDFs)

## Create a place index resource
<a name="aurora-create-place-index"></a>

Start by creating a place index resource to support geocoding queries.

1. Open the Amazon Location Service console at [https://console.aws.amazon.com/location/](https://console.aws.amazon.com/location/home).

1. In the left navigation pane, choose **Place indexes**.

1. Fill out the following boxes:
   + ** Name** – Enter a name for the place index resource. For example, {{AuroraPlaceIndex}}. Maximum 100 characters. Valid entries include alphanumeric characters, hyphens, periods, and underscores.
   + ** Description** – Enter an optional description. For example, {{Place index for Amazon Aurora}}.

1. Under **Data providers**, choose an available [data provider](https://aws.amazon.com/location/data-providers/) to use with your place index resource. If you have no preference, we recommend starting with {{Esri}}.

1. Under **Data storage options**, specify **Yes, results will be stored**. This indicates that you intend to save the geocoding results in a database.

1. (Optional) Under **Tags**, enter a tag **Key** and **Value**. This adds a tag your new place index resource. For more information, see [Tagging your resources](tagging.md).

1. Choose **Create place index**.

## Create an AWS Lambda function for geocoding
<a name="aurora-create-lambda"></a>

To create a connection between Amazon Aurora PostgreSQL and Amazon Location Service, you need an AWS Lambda function to handle requests from the database engine. This function translates the Lambda user-defined function event and calls the Amazon Location operation `SearchPlaceIndexForText`.

You can create the function using the AWS Lambda console, the AWS Command Line Interface, or the AWS Lambda APIs.

**To create a Lambda user-defined function using the console**

1. Open the AWS Lambda console at [https://console.aws.amazon.com/lambda/](https://console.aws.amazon.com/lambda/home).

1. From the left navigation, choose **Functions**.

1.  Choose **Create Function**, and make sure that **Author from scratch** is selected.

1. Fill out the following boxes:
   + **Function name** – Enter a unique name for your function. Valid entries include alphanumeric characters, hyphens, and underscores with no spaces. For example, {{AuroraGeocoder}}.
   + **Runtime** – Choose {{Python 3.8}}.

1. Choose **Create function**.

1. Choose the **Code** tab to open the editor.

1. Overwrite the placeholder code in `lambda_function.py` with the following:

   ```
   from os import environ

   import boto3
   from botocore.config import Config

   # load the place index name from the environment, falling back to a default
   PLACE_INDEX_NAME = environ.get("PLACE_INDEX_NAME", "AuroraPlaceIndex")

   location = boto3.client("location", config=Config(user_agent="Amazon Aurora PostgreSQL"))

   """
   This Lambda function receives a payload from Amazon Aurora and translates it to
   an Amazon Location `SearchPlaceIndex` call and returns the results as-is, to be
   post-processed by a PL/pgSQL function.
   """
   def lambda_handler(event, context):
       kwargs = {}

       if event.get("biasPosition") is not None:
           kwargs["BiasPosition"] = event["biasPosition"]

       if event.get("filterBBox") is not None:
           kwargs["FilterBBox"] = event["filterBBox"]

       if event.get("filterCountries") is not None:
           kwargs["FilterCountries"] = event["filterCountries"]

       if event.get("maxResults") is not None:
           kwargs["MaxResults"] = event["maxResults"]

       return location.search_place_index_for_text(
           IndexName=PLACE_INDEX_NAME,
           Text=event["text"],
           **kwargs)["Results"]
   ```

1. If you've named your place index something other than {{AuroraPlaceIndex}}, create an environment variable named `PLACE_INDEX_NAME` to assign the resource name to:
   + From the **Configuration** tab, choose **Environment Variables**.
   + Choose **Edit**, then choose **Add environment variable**.
   + For **Key**: Enter `PLACE_INDEX_NAME`.
   + For **Value**: Enter the name of your place index resource.

1. Choose **Deploy** to save the updated function.

1. From the **Test** drop-down menu, choose **Configure test Event**.

1. Choose **Create new test event**.

1. Enter the following test event:

   ```
   {
     "text": "Baker Beach",
     "biasPosition": [-122.483, 37.790],
     "filterCountries": ["USA"]
   }
   ```

1. Choose **Test** to test the Lambda function.

1. Choose the **Configuration** tab.

1. Under **General configuration**: Choose **Permissions**.

1. Under **Execution role**: Choose the hyper linked **Role name** to grant Amazon Location Service permissions to your Lambda function.

1. Under the **Permissions** tab: Select the **Add permissions** drop down, then choose **Create inline policy**.

1. Choose the **JSON** tab.

1. Add the following IAM policy:
   + The following policy gives permission to send `SearchPlaceIndexForText` to the place index resource {{AuroraPlaceIndex}}.

     ```
     {
       "Version": "2012-10-17",
       "Statement": [
         {
           "Effect": "Allow",
           "Action": "geo:SearchPlaceIndexForText",
           "Resource": "arn:aws:geo:<Region>:<AccountId>:place-index/{{AuroraPlaceIndex}}"
         }
       ]
     }
     ```

1. Choose **Review policy**.

1. Enter a policy name. For example, {{AuroraPlaceIndexReadOnly}}.

1. Choose **Create policy**.

## Grant Amazon Aurora PostgreSQL access to AWS Lambda
<a name="aurora-invoke-API"></a>

Before Amazon Aurora PostgreSQL can invoke an AWS Lambda function, you must grant access permission.

If your Amazon Aurora PostgreSQL cluster isn't publicly accessible, you will need to first create a VPC endpoint for AWS Lambda in order for Amazon Aurora to call your Lambda function.

**Create a VPC Endpoint for AWS Lambda**

**Note**
This step is only required if your Amazon Aurora PostgreSQL cluster isn't publicly accessible.

1. Open the [Amazon Virtual Private Cloud Console](https://console.aws.amazon.com/vpc/home).

1. In the left navigation, choose **Endpoints**.

1. Choose **Create endpoint**.

1. In the **Service Name** filter, enter "lambda", then choose `com.amazonaws.<region>.lambda`.

1. Choose the VPC containing your Aurora cluster.

1. Choose a subnet for each availability zone.

1. In the **Security group** filter, enter "default" or the name of the security group your Aurora cluster is a member of, then choose the security group.

1. Choose **Create endpoint**.

**Create an IAM policy to grant permission to invoke your AWS Lambda function**

1. Open the [IAM console](https://console.aws.amazon.com/iam/home#/home).

1. In the left navigation, expand **Access Management** to choose **Policies**.

1. Choose **Create policy**.

1. On the **JSON** tab, input the following policy:
   + The following is an example of an IAM policy that grants Amazon Aurora PostgreSQL permission to invoke the `AuroraGeocoder` AWS Lambda function.

   ```
   {
       "Version": "2012-10-17",
       "Statement": [
           {
               "Effect": "Allow",
               "Action": "lambda:InvokeFunction",
               "Resource": [
                   "arn:aws:lambda:<Region>:<AccountId>:function:{{AuroraGeocoder}}"
               ]
           }
       ]
   }
   ```

1. Choose **Next: Tags** to add optional tags.

1. Choose **Next: Review**.

1. Review your policy and enter the following details for the policy:
   + **Name** – Use alphanumeric and '\+=,.@-\_' characters. Maximum 128 characters. For example, {{AuroraGeocoderInvoke}}.
   + **Description** – Enter an optional description. Use alphanumeric and '\+=,.@-\_' characters. Maximum 1000 characters.

1. Choose **Create policy**. Note the ARN for this policy, which you use to attach the policy to an IAM role.

**Create an IAM role to give permission to Amazon Relational Database Service (Amazon RDS)**

By creating an IAM role, Amazon Aurora PostgreSQL can assume the role on your behalf to access your Lambda function. For more information, see [Creating a role to delegate permissions to an IAM user](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html) in the *IAM User Guide*.

The following example is an AWS CLI command that creates a role named {{AuroraGeocoderInvokeRole}}:

```
aws iam create-role  --role-name rds-lambda-role --assume-role-policy-document '{
    "Version": "2012-10-17",
    "Statement": [
        {
        "Effect": "Allow",
        "Principal": {
            "Service": "rds.amazonaws.com"
        },
        "Action": "sts:AssumeRole"
        }
    ]
}'
```

**Attach your IAM policy to the IAM role**

When you have an IAM role, attach the IAM policy that you've created.

The following example is an AWS CLI command that attaches the policy {{AuroraGeocoderInvoke}} to the role {{AuroraGeocoderInvokeRole}}.

```
aws iam attach-role-policy  --policy-arn {{AuroraGeocoderInvoke}}  --role-name {{AuroraGeocoderInvokeRole}}
```

**Add the IAM role to a Amazon Aurora DB cluster**

The following example is an AWS CLI command to add an IAM role to a Amazon Aurora PostgreSQL DB cluster named {{MyAuroraCluster}}.

```
aws rds add-role-to-db-cluster \
--db-cluster-identifier {{MyAuroraCluster}} \
--feature-name Lambda \
--role-arn {{AuroraGeocoderInvokeRole}}   \
--region your-region
```

## Invoke the AWS Lambda function
<a name="aurora-setup-table"></a>

After you grant permission to Amazon Aurora PostgreSQL to invoke your geocoding Lambda function, you can create an Amazon Aurora PostgreSQL user-defined function to invoke the geocoding AWS Lambda function. For more information, see [Invoking an AWS Lambda function from an Amazon Aurora PostgreSQL DB cluster](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/PostgreSQL-Lambda.html) in the *Amazon Aurora User Guide*.

**Install the required PostgreSQL extensions**

To install the required PostgreSQL extensions `aws_lambda` and `aws _commons` extensions, see [Overview of using a Lambda function](https://docs.aws.amazon.com/AmazonRDS/latest/AuroraUserGuide/PostgreSQL-Lambda.html#PostgreSQL-Lambda-overview) in the *Amazon Aurora User Guide*.

```
CREATE EXTENSION IF NOT EXISTS aws_lambda CASCADE;
```

**Install the required PostGIS extensions**

PostGIS is an extension to PostgreSQL for storing and managing spatial information. For more information, see [Working with the PostGIS extension](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.PostgreSQL.CommonDBATasks.PostGIS.html) on the *Amazon Relational Database Service User Guide*.

```
CREATE EXTENSION IF NOT EXISTS postgis;
```

**Create an SQL user-defined function that invokes the Lambda function**

In an SQL editor, create a new user-defined function `f_SearchPlaceIndexForText` to invoke the function {{AuroraGeocoder}}:

```
CREATE OR REPLACE FUNCTION f_SearchPlaceIndexForText(
  text text,
  bias_position geometry(Point, 4326) DEFAULT NULL,
  filter_bbox box2d DEFAULT NULL,
  filter_countries text[] DEFAULT NULL,
  max_results int DEFAULT 1
)
 RETURNS TABLE (
   label text,
   address_number text,
   street text,
   municipality text,
   postal_code text,
   sub_region text,
   region text,
   country text,
   geom geometry(Point, 4326)
 )
 LANGUAGE plpgsql
 IMMUTABLE
AS $function$
begin
    RETURN QUERY
    WITH results AS (
      SELECT json_array_elements(payload) rsp
      FROM aws_lambda.invoke(
        aws_commons.create_lambda_function_arn('{{AuroraGeocoder}}'),
        json_build_object(
          'text', text,
          'biasPosition',
          CASE WHEN bias_position IS NOT NULL THEN
            array_to_json(ARRAY[ST_X(bias_position), ST_Y(bias_position)])
          END,
          'filterBBox',
          CASE WHEN filter_bbox IS NOT NULL THEN
            array_to_json(ARRAY[ST_XMin(filter_bbox), ST_YMin(filter_bbox), ST_XMax(filter_bbox), ST_YMax(filter_bbox)])
          END,
          'filterCountries', filter_countries,
          'maxResults', max_results
        )
      )
    )
    SELECT
      rsp->'Place'->>'Label' AS label,
      rsp->'Place'->>'AddressNumber' AS address_number,
      rsp->'Place'->>'Street' AS street,
      rsp->'Place'->>'Municipality' AS municipality,
      rsp->'Place'->>'PostalCode' AS postal_code,
      rsp->'Place'->>'SubRegion' AS sub_region,
      rsp->'Place'->>'Region' AS region,
      rsp->'Place'->>'Country' AS country,
      ST_GeomFromGeoJSON(
        json_build_object(
          'type', 'Point',
            'coordinates', rsp->'Place'->'Geometry'->'Point'
        )
      ) geom
    FROM results;
end;
$function$;
```

**Call the SQL function to geocode from Aurora**

Running the SQL statement invokes the Lambda function {{AuroraGeocoder}}, which takes address records from the database table in the Amazon Aurora PostgreSQL database and geocodes them using a place index resource.

**Note**
Amazon Aurora PostgreSQL invokes the Lambda function for each call to the SQL user-defined function.
If you are geocoding 50 rows, Amazon Aurora PostgreSQL invokes the Lambda function 50 times. One invocation for each row.

The following `f_SearchPlaceIndexForText` SQL function makes requests to Amazon Location's `[SearchPlaceIndexForText](https://docs.aws.amazon.com/location-places/latest/APIReference/API_SearchPlaceIndexForText.html)` API through the {{AuroraGeocoder}} Lambda function. The function returns a `geom` column that's a PostGIS geometry, which `ST_AsText(geom)` converts to text.

```
SELECT *, ST_AsText(geom)
FROM f_SearchPlaceIndexForText('Vancouver, BC');
```

By default, the return will contain one row. To request additional rows, up to the `MaxResults` limit, run the following SQL statement while providing a `BiasPosition` and limiting to results in Canada.

```
SELECT *
FROM f_SearchPlaceIndexForText('Mount Pleasant', ST_MakePoint(-123.113, 49.260), null, '{"CAN"}', 5);
```

To filter results using a bounding box, then pass a `[Box2D](https://postgis.net/docs/Box2D.html)` as `filter_bbox`:
+ `[FilterBBox](https://docs.aws.amazon.com/location-places/latest/APIReference/API_SearchPlaceIndexForText.html#locationplaces-SearchPlaceIndexForText-request-FilterBBox)` – Filters the results by returning places within a bounding box. This is an optional parameter.

```
SELECT *
FROM f_SearchPlaceIndexForText('Mount Pleasant', null, 'BOX(-139.06 48.30, -114.03 60.00)'::box2d, '{"CAN"}', 5);
```

For more information on PostGIS types and functions, see the [PostGIS Reference](https://postgis.net/docs/reference.html).

## Enriching a database containing address data
<a name="aurora-run-sql"></a>

You can construct a formatted address and simultaneously normalize and geocode using the Amazon Location operation `SearchPlaceIndexForText` given a database table with the following data broken out into the following columns:
+ `id`
+ `address`
+ `city`
+ `state`
+ `zip`

```
WITH source_data AS (
  SELECT
    id,
    address || ', ' || city || ', ' || state || ', ' || zip AS formatted_address
  FROM addresses
),
geocoded_data AS (
  SELECT
    *,
    (f_SearchPlaceIndexForText(formatted_address)).*
  FROM source_data
)
SELECT
  id,
  formatted_address,
  label normalized_address,
  ST_Y(geom) latitude,
  ST_X(geom) longitude
FROM geocoded_data
-- limit the number of rows that will be geocoded; remove this to geocode the entire table
LIMIT 1;
```

The following example illustrates one resulting datatable row:

```
 id |      formatted_address         |            normalized_address              |     latitude     |     longitude
----+--------------------------------+--------------------------------------------+------------------+-------------------
 42 | 123 Anytown Ave N, Seattle, WA | 123 Anytown Ave N, Seattle, WA, 12345, USA | 47.6223000127926 | -122.336745971039
(1 row)
```

**Update the database table and populate columns**

The following example updates the table and populates columns with results of `SearchPlaceIndexForText` queries:

```
WITH source_data AS (
  -- select rows that have not been geocoded and created a formatted address for each
  SELECT
    id,
    address || ', ' || city || ', ' || state || ', ' || zip AS formatted_address
  FROM addresses
  WHERE label IS NULL
  -- limit the number of rows that will be geocoded; remove this to geocode the entire table
  LIMIT 1
),
geocoded_data AS (
  -- geocode each row and keep it linked to the source's ID
  SELECT
    id,
    (f_SearchPlaceIndexForText(formatted_address)).*
  FROM source_data
)
UPDATE addresses
-- populate columns
SET
  normalized_address = geocoded_data.label,
  latitude = ST_Y(geocoded_data.geom),
  longitude = ST_X(geocoded_data.geom)
FROM geocoded_data
-- ensure that rows match
WHERE addresses.id = geocoded_data.id;
```

## Next steps
<a name="aurora-amazon-location-next-steps"></a>

Sample code is available in the Amazon Location Service samples repository on [GitHub](https://github.com/aws-samples/amazon-location-samples/tree/main/aurora-udfs), which includes [an AWS CloudFormation template](https://github.com/aws-samples/amazon-location-samples/tree/main/aurora-udfs/cloudformation/template.yaml).
