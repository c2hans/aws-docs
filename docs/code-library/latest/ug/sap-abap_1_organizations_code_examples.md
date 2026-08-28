---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/sap-abap_1_organizations_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Organizations examples using SDK for SAP ABAP
<a name="sap-abap_1_organizations_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for SAP ABAP with Organizations.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `AttachPolicy`
<a name="organizations_AttachPolicy_sap-abap_1_topic"></a>

The following code example shows how to use `AttachPolicy`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/org#code-examples).

```
    TRY.
        lo_org->attachpolicy(
          iv_policyid = iv_policy_id
          iv_targetid = iv_target_id ).
        MESSAGE 'Policy attached to target.' TYPE 'I'.
      CATCH /aws1/cx_orgaccessdeniedex.
        MESSAGE 'You do not have permission to attach the policy.' TYPE 'E'.
      CATCH /aws1/cx_orgpolicynotfoundex.
        MESSAGE 'The specified policy does not exist.' TYPE 'E'.
      CATCH /aws1/cx_orgtargetnotfoundex.
        MESSAGE 'The specified target does not exist.' TYPE 'E'.
      CATCH /aws1/cx_orgduplicateplyatta00.
        MESSAGE 'The policy is already attached to the target.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [AttachPolicy](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `CreatePolicy`
<a name="organizations_CreatePolicy_sap-abap_1_topic"></a>

The following code example shows how to use `CreatePolicy`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/org#code-examples).

```
    TRY.
        oo_result = lo_org->createpolicy(       " oo_result is returned for testing purposes. "
          iv_name        = iv_policy_name
          iv_description = iv_policy_description
          iv_content     = iv_policy_content
          iv_type        = iv_policy_type ).
        MESSAGE 'Policy created.' TYPE 'I'.
      CATCH /aws1/cx_orgaccessdeniedex.
        MESSAGE 'You do not have permission to create a policy.' TYPE 'E'.
      CATCH /aws1/cx_orgduplicatepolicyex.
        MESSAGE 'A policy with this name already exists.' TYPE 'E'.
      CATCH /aws1/cx_orgmalformedplydocex.
        MESSAGE 'The policy content is malformed.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [CreatePolicy](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `DeletePolicy`
<a name="organizations_DeletePolicy_sap-abap_1_topic"></a>

The following code example shows how to use `DeletePolicy`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/org#code-examples).

```
    TRY.
        lo_org->deletepolicy(
          iv_policyid = iv_policy_id ).
        MESSAGE 'Policy deleted.' TYPE 'I'.
      CATCH /aws1/cx_orgaccessdeniedex.
        MESSAGE 'You do not have permission to delete the policy.' TYPE 'E'.
      CATCH /aws1/cx_orgpolicynotfoundex.
        MESSAGE 'The specified policy does not exist.' TYPE 'E'.
      CATCH /aws1/cx_orgpolicyinuseex.
        MESSAGE 'The policy is still attached to one or more targets.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [DeletePolicy](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `DescribePolicy`
<a name="organizations_DescribePolicy_sap-abap_1_topic"></a>

The following code example shows how to use `DescribePolicy`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/org#code-examples).

```
    TRY.
        oo_result = lo_org->describepolicy(     " oo_result is returned for testing purposes. "
          iv_policyid = iv_policy_id ).
        DATA(lo_policy) = oo_result->get_policy( ).
        MESSAGE 'Retrieved policy details.' TYPE 'I'.
      CATCH /aws1/cx_orgaccessdeniedex.
        MESSAGE 'You do not have permission to describe the policy.' TYPE 'E'.
      CATCH /aws1/cx_orgpolicynotfoundex.
        MESSAGE 'The specified policy does not exist.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [DescribePolicy](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `DetachPolicy`
<a name="organizations_DetachPolicy_sap-abap_1_topic"></a>

The following code example shows how to use `DetachPolicy`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/org#code-examples).

```
    TRY.
        lo_org->detachpolicy(
          iv_policyid = iv_policy_id
          iv_targetid = iv_target_id ).
        MESSAGE 'Policy detached from target.' TYPE 'I'.
      CATCH /aws1/cx_orgaccessdeniedex.
        MESSAGE 'You do not have permission to detach the policy.' TYPE 'E'.
      CATCH /aws1/cx_orgpolicynotfoundex.
        MESSAGE 'The specified policy does not exist.' TYPE 'E'.
      CATCH /aws1/cx_orgtargetnotfoundex.
        MESSAGE 'The specified target does not exist.' TYPE 'E'.
      CATCH /aws1/cx_orgpolicynotattex.
        MESSAGE 'The policy is not attached to the target.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [DetachPolicy](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `ListPolicies`
<a name="organizations_ListPolicies_sap-abap_1_topic"></a>

The following code example shows how to use `ListPolicies`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/org#code-examples).

```
    TRY.
        oo_result = lo_org->listpolicies(       " oo_result is returned for testing purposes. "
          iv_filter = iv_filter ).
        DATA(lt_policies) = oo_result->get_policies( ).
        MESSAGE 'Retrieved list of policies.' TYPE 'I'.
      CATCH /aws1/cx_orgaccessdeniedex.
        MESSAGE 'You do not have permission to list policies.' TYPE 'E'.
      CATCH /aws1/cx_orgawsorgsnotinuseex.
        MESSAGE 'Your account is not a member of an organization.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [ListPolicies](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
