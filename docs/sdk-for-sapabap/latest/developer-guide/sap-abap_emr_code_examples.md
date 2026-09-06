---
source_url: https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/sap-abap_emr_code_examples.html
---

# Amazon EMR examples using SDK for SAP ABAP
<a name="sap-abap_emr_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for SAP ABAP with Amazon EMR.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `AddJobFlowSteps`
<a name="emr_AddJobFlowSteps_sap-abap_topic"></a>

The following code example shows how to use `AddJobFlowSteps`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/emr#code-examples).

```
    TRY.
        " Build args list for Spark submit
        DATA lt_args TYPE /aws1/cl_emrxmlstringlist_w=>tt_xmlstringlist.
        APPEND NEW /aws1/cl_emrxmlstringlist_w( 'spark-submit' ) TO lt_args.
        APPEND NEW /aws1/cl_emrxmlstringlist_w( '--deploy-mode' ) TO lt_args.
        APPEND NEW /aws1/cl_emrxmlstringlist_w( 'cluster' ) TO lt_args.
        APPEND NEW /aws1/cl_emrxmlstringlist_w( iv_script_uri ) TO lt_args.
        APPEND LINES OF it_script_args TO lt_args.

        " Create step configuration
        DATA(lo_hadoop_jar_step) = NEW /aws1/cl_emrhadoopjarstepcfg(
          iv_jar = 'command-runner.jar'
          it_args = lt_args
        ).

        DATA(lo_step_config) = NEW /aws1/cl_emrstepconfig(
          iv_name = iv_name
          iv_actiononfailure = 'CONTINUE'
          io_hadoopjarstep = lo_hadoop_jar_step
        ).

        DATA lt_steps TYPE /aws1/cl_emrstepconfig=>tt_stepconfiglist.
        APPEND lo_step_config TO lt_steps.

        DATA(lo_result) = lo_emr->addjobflowsteps(
          iv_jobflowid = iv_cluster_id
          it_steps = lt_steps
        ).

        " Get first step ID
        DATA(lt_step_ids) = lo_result->get_stepids( ).
        READ TABLE lt_step_ids INDEX 1 INTO DATA(lo_step_id_obj).
        IF sy-subrc = 0.
          ov_step_id = lo_step_id_obj->get_value( ).
          MESSAGE |Step added with ID { ov_step_id }| TYPE 'I'.
        ENDIF.
      CATCH /aws1/cx_emrinternalservererr INTO DATA(lo_internal_error).
        DATA(lv_error) = lo_internal_error->if_message~get_text( ).
        MESSAGE lv_error TYPE 'E'.
    ENDTRY.
```
+  For API details, see [AddJobFlowSteps](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `DescribeCluster`
<a name="emr_DescribeCluster_sap-abap_topic"></a>

The following code example shows how to use `DescribeCluster`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/emr#code-examples).

```
    TRY.
        oo_result = lo_emr->describecluster(
          iv_clusterid = iv_cluster_id
        ).
        DATA(lo_cluster) = oo_result->get_cluster( ).
        DATA(lv_cluster_name) = lo_cluster->get_name( ).
        MESSAGE |Retrieved cluster information for { lv_cluster_name }| TYPE 'I'.
      CATCH /aws1/cx_emrinternalserverex INTO DATA(lo_internal_error).
        DATA(lv_error) = lo_internal_error->if_message~get_text( ).
        MESSAGE lv_error TYPE 'E'.
      CATCH /aws1/cx_emrinvalidrequestex INTO DATA(lo_invalid_error).
        lv_error = lo_invalid_error->if_message~get_text( ).
        MESSAGE lv_error TYPE 'E'.
    ENDTRY.
```
+  For API details, see [DescribeCluster](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `DescribeStep`
<a name="emr_DescribeStep_sap-abap_topic"></a>

The following code example shows how to use `DescribeStep`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/emr#code-examples).

```
    TRY.
        oo_result = lo_emr->describestep(
          iv_clusterid = iv_cluster_id
          iv_stepid = iv_step_id
        ).
        DATA(lo_step) = oo_result->get_step( ).
        DATA(lv_step_name) = lo_step->get_name( ).
        MESSAGE |Retrieved step information for { lv_step_name }| TYPE 'I'.
      CATCH /aws1/cx_emrinternalserverex INTO DATA(lo_internal_error).
        DATA(lv_error) = lo_internal_error->if_message~get_text( ).
        MESSAGE lv_error TYPE 'E'.
      CATCH /aws1/cx_emrinvalidrequestex INTO DATA(lo_invalid_error).
        lv_error = lo_invalid_error->if_message~get_text( ).
        MESSAGE lv_error TYPE 'E'.
    ENDTRY.
```
+  For API details, see [DescribeStep](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `ListSteps`
<a name="emr_ListSteps_sap-abap_topic"></a>

The following code example shows how to use `ListSteps`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/emr#code-examples).

```
    TRY.
        oo_result = lo_emr->liststeps(
          iv_clusterid = iv_cluster_id
        ).
        DATA(lt_steps) = oo_result->get_steps( ).
        DATA(lv_step_count) = lines( lt_steps ).
        MESSAGE |Retrieved { lv_step_count } steps for cluster| TYPE 'I'.
      CATCH /aws1/cx_emrinternalserverex INTO DATA(lo_internal_error).
        DATA(lv_error) = lo_internal_error->if_message~get_text( ).
        MESSAGE lv_error TYPE 'E'.
      CATCH /aws1/cx_emrinvalidrequestex INTO DATA(lo_invalid_error).
        lv_error = lo_invalid_error->if_message~get_text( ).
        MESSAGE lv_error TYPE 'E'.
    ENDTRY.
```
+  For API details, see [ListSteps](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `RunJobFlow`
<a name="emr_RunJobFlow_sap-abap_topic"></a>

The following code example shows how to use `RunJobFlow`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/emr#code-examples).

```
    TRY.
        " Create instances configuration
        DATA(lo_instances) = NEW /aws1/cl_emrjobflowinstsconfig(
          iv_masterinstancetype = 'm5.xlarge'
          iv_slaveinstancetype = 'm5.xlarge'
          iv_instancecount = 3
          iv_keepjobflowalivewhennos00 = iv_keep_alive
          iv_emrmanagedmastersecgroup = iv_primary_sec_grp
          iv_emrmanagedslavesecgroup = iv_secondary_sec_grp
        ).

        DATA(lo_result) = lo_emr->runjobflow(
          iv_name = iv_name
          iv_loguri = iv_log_uri
          iv_releaselabel = 'emr-5.30.1'
          io_instances = lo_instances
          it_steps = it_steps
          it_applications = it_applications
          iv_jobflowrole = iv_job_flow_role
          iv_servicerole = iv_service_role
          iv_ebsrootvolumesize = 10
          iv_visibletoallusers = abap_true
        ).

        ov_cluster_id = lo_result->get_jobflowid( ).
        MESSAGE 'EMR cluster created successfully.' TYPE 'I'.
      CATCH /aws1/cx_emrinternalservererr INTO DATA(lo_internal_error).
        DATA(lv_error) = lo_internal_error->if_message~get_text( ).
        MESSAGE lv_error TYPE 'E'.
      CATCH /aws1/cx_emrclientexc INTO DATA(lo_client_error).
        lv_error = lo_client_error->if_message~get_text( ).
        MESSAGE lv_error TYPE 'E'.
    ENDTRY.
```
+  For API details, see [RunJobFlow](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `TerminateJobFlows`
<a name="emr_TerminateJobFlows_sap-abap_topic"></a>

The following code example shows how to use `TerminateJobFlows`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/emr#code-examples).

```
    TRY.
        DATA lt_cluster_ids TYPE /aws1/cl_emrxmlstringlist_w=>tt_xmlstringlist.
        APPEND NEW /aws1/cl_emrxmlstringlist_w( iv_cluster_id ) TO lt_cluster_ids.

        lo_emr->terminatejobflows(
          it_jobflowids = lt_cluster_ids
        ).
        MESSAGE 'EMR cluster terminated successfully.' TYPE 'I'.
      CATCH /aws1/cx_emrinternalservererr INTO DATA(lo_internal_error).
        DATA(lv_error) = lo_internal_error->if_message~get_text( ).
        MESSAGE lv_error TYPE 'E'.
    ENDTRY.
```
+  For API details, see [TerminateJobFlows](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.
