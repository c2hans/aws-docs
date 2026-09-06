---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/sap-abap_1_aurora_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Aurora examples using SDK for SAP ABAP
<a name="sap-abap_1_aurora_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for SAP ABAP with Aurora.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `CreateDBClusterParameterGroup`
<a name="aurora_CreateDBClusterParameterGroup_sap-abap_1_topic"></a>

The following code example shows how to use `CreateDBClusterParameterGroup`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/rds#code-examples).

```
    TRY.
        DATA(lo_output) = lo_rds->createdbclusterparamgroup(
          iv_dbclusterparamgroupname = iv_param_group_name
          iv_dbparametergroupfamily = iv_param_group_family
          iv_description = iv_description
        ).
        oo_result = lo_output->get_dbclusterparametergroup( ).
      CATCH /aws1/cx_rdsdbparmgralrexfault.
        " Re-raise exception - parameter group already exists
        RAISE EXCEPTION TYPE /aws1/cx_rdsdbparmgralrexfault.
      CATCH /aws1/cx_rdsdbprmgrquotaexcd00.
        " Re-raise exception - quota exceeded
        RAISE EXCEPTION TYPE /aws1/cx_rdsdbprmgrquotaexcd00.
    ENDTRY.
```
+  For API details, see [CreateDBClusterParameterGroup](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `DeleteDBClusterParameterGroup`
<a name="aurora_DeleteDBClusterParameterGroup_sap-abap_1_topic"></a>

The following code example shows how to use `DeleteDBClusterParameterGroup`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/rds#code-examples).

```
    TRY.
        lo_rds->deletedbclusterparamgroup(
          iv_dbclusterparamgroupname = iv_param_group_name
        ).
      CATCH /aws1/cx_rdsdbprmgrnotfndfault.
        " Re-raise exception - parameter group not found
        RAISE EXCEPTION TYPE /aws1/cx_rdsdbprmgrnotfndfault.
      CATCH /aws1/cx_rdsinvdbprmgrstatef00.
        " Re-raise exception - invalid state
        RAISE EXCEPTION TYPE /aws1/cx_rdsinvdbprmgrstatef00.
    ENDTRY.
```
+  For API details, see [DeleteDBClusterParameterGroup](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `DescribeDBClusterParameterGroups`
<a name="aurora_DescribeDBClusterParameterGroups_sap-abap_1_topic"></a>

The following code example shows how to use `DescribeDBClusterParameterGroups`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/rds#code-examples).

```
    TRY.
        DATA(lo_output) = lo_rds->describedbclusterparamgroups(
          iv_dbclusterparamgroupname = iv_param_group_name
        ).
        DATA(lt_param_groups) = lo_output->get_dbclusterparametergroups( ).
        IF lines( lt_param_groups ) > 0.
          oo_result = lt_param_groups[ 1 ].
        ENDIF.
      CATCH /aws1/cx_rdsdbprmgrnotfndfault.
    ENDTRY.
```
+  For API details, see [DescribeDBClusterParameterGroups](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `DescribeDBClusterParameters`
<a name="aurora_DescribeDBClusterParameters_sap-abap_1_topic"></a>

The following code example shows how to use `DescribeDBClusterParameters`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/rds#code-examples).

```
    TRY.
        DATA lv_marker TYPE /aws1/rdsstring VALUE ''.
        DATA lt_all_parameters TYPE /aws1/cl_rdsparameter=>tt_parameterslist.

        DO.
          DATA(lo_output) = lo_rds->describedbclusterparameters(
            iv_dbclusterparamgroupname = iv_param_group_name
            iv_source = iv_source
            iv_marker = lv_marker
          ).

          LOOP AT lo_output->get_parameters( ) INTO DATA(lo_param).
            IF iv_name_prefix IS INITIAL OR
               lo_param->get_parametername( ) CP |{ iv_name_prefix }*|.
              APPEND lo_param TO lt_all_parameters.
            ENDIF.
          ENDLOOP.

          lv_marker = lo_output->get_marker( ).
          IF lv_marker IS INITIAL.
            EXIT.
          ENDIF.
        ENDDO.

        ot_parameters = lt_all_parameters.
      CATCH /aws1/cx_rdsdbprmgrnotfndfault.
        " Re-raise exception - parameter group not found
        RAISE EXCEPTION TYPE /aws1/cx_rdsdbprmgrnotfndfault.
    ENDTRY.
```
+  For API details, see [DescribeDBClusterParameters](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `DescribeDBEngineVersions`
<a name="aurora_DescribeDBEngineVersions_sap-abap_1_topic"></a>

The following code example shows how to use `DescribeDBEngineVersions`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/rds#code-examples).

```
    " iv_engine                 = 'mysql'
    " iv_dbparametergroupfamily = 'mysql8.0' (optional - filters by parameter group family)
    TRY.
        oo_result = lo_rds->describedbengineversions(
          iv_engine                 = iv_engine
          iv_dbparametergroupfamily = iv_dbparametergroupfamily ).
        DATA(lv_version_count) = lines( oo_result->get_dbengineversions( ) ).
        MESSAGE |Retrieved { lv_version_count } engine versions.| TYPE 'I'.
    ENDTRY.
```
+  For API details, see [DescribeDBEngineVersions](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `DescribeOrderableDBInstanceOptions`
<a name="aurora_DescribeOrderableDBInstanceOptions_sap-abap_1_topic"></a>

The following code example shows how to use `DescribeOrderableDBInstanceOptions`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/rds#code-examples).

```
    " iv_engine        = 'mysql'
    " iv_engineversion = '8.0.35'
    TRY.
        oo_result = lo_rds->descrorderabledbinstoptions(
          iv_engine        = iv_engine
          iv_engineversion = iv_engineversion ).
        DATA(lv_option_count) = lines( oo_result->get_orderabledbinstoptions( ) ).
        MESSAGE |Retrieved { lv_option_count } orderable DB instance options.| TYPE 'I'.
    ENDTRY.
```
+  For API details, see [DescribeOrderableDBInstanceOptions](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `ModifyDBClusterParameterGroup`
<a name="aurora_ModifyDBClusterParameterGroup_sap-abap_1_topic"></a>

The following code example shows how to use `ModifyDBClusterParameterGroup`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/rds#code-examples).

```
    TRY.
        oo_result = lo_rds->modifydbclusterparamgroup(
          iv_dbclusterparamgroupname = iv_param_group_name
          it_parameters = it_update_parameters
        ).
      CATCH /aws1/cx_rdsdbprmgrnotfndfault.
        " Re-raise exception - parameter group not found
        RAISE EXCEPTION TYPE /aws1/cx_rdsdbprmgrnotfndfault.
      CATCH /aws1/cx_rdsinvdbprmgrstatef00.
        " Re-raise exception - invalid state
        RAISE EXCEPTION TYPE /aws1/cx_rdsinvdbprmgrstatef00.
    ENDTRY.
```
+  For API details, see [ModifyDBClusterParameterGroup](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.
