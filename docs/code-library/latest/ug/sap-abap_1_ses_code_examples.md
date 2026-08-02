---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/sap-abap_1_ses_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Amazon SES examples using SDK for SAP ABAP
<a name="sap-abap_1_ses_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for SAP ABAP with Amazon SES.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `CreateReceiptFilter`
<a name="ses_CreateReceiptFilter_sap-abap_1_topic"></a>

The following code example shows how to use `CreateReceiptFilter`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ses#code-examples).

```
    " iv_allow = abap_true means 'Allow', abap_false means 'Block'
    DATA(lv_policy) = COND /aws1/sesreceiptfilterpolicy(
      WHEN iv_allow = abap_true THEN 'Allow'
      ELSE 'Block'
    ).

    DATA(lo_ip_filter) = NEW /aws1/cl_sesreceiptipfilter(
      iv_policy = lv_policy
      iv_cidr = iv_ip_address_or_range
    ).

    DATA(lo_filter) = NEW /aws1/cl_sesreceiptfilter(
      iv_name = iv_filter_name
      io_ipfilter = lo_ip_filter
    ).

    TRY.
        lo_ses->createreceiptfilter( io_filter = lo_filter ).
        MESSAGE 'Receipt filter created successfully' TYPE 'I'.
      CATCH /aws1/cx_sesalreadyexistsex INTO DATA(lo_ex1).
        DATA(lv_error) = |Filter already exists: { lo_ex1->get_text( ) }|.
        MESSAGE lv_error TYPE 'I'.
        RAISE EXCEPTION lo_ex1.
      CATCH /aws1/cx_rt_generic INTO DATA(lo_ex_generic).
        lv_error = |An error occurred: { lo_ex_generic->get_text( ) }|.
        MESSAGE lv_error TYPE 'I'.
        RAISE EXCEPTION lo_ex_generic.
    ENDTRY.
```
+  For API details, see [CreateReceiptFilter](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `CreateReceiptRule`
<a name="ses_CreateReceiptRule_sap-abap_1_topic"></a>

The following code example shows how to use `CreateReceiptRule`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ses#code-examples).

```
    " Create S3 action for copying emails to S3
    DATA(lo_s3_action) = NEW /aws1/cl_sess3action(
      iv_bucketname = iv_bucket_name
      iv_objectkeyprefix = iv_prefix
    ).

    " Create receipt action with S3 action
    DATA(lo_action) = NEW /aws1/cl_sesreceiptaction(
      io_s3action = lo_s3_action
    ).

    " Create list of actions
    DATA lt_actions TYPE /aws1/cl_sesreceiptaction=>tt_receiptactionslist.
    APPEND lo_action TO lt_actions.

    " Create receipt rule
    DATA(lo_rule) = NEW /aws1/cl_sesreceiptrule(
      iv_name = iv_rule_name
      iv_enabled = abap_true
      it_recipients = it_recipients
      it_actions = lt_actions
    ).

    TRY.
        lo_ses->createreceiptrule(
          iv_rulesetname = iv_rule_set_name
          io_rule = lo_rule
        ).
        MESSAGE 'Receipt rule created successfully' TYPE 'I'.
      CATCH /aws1/cx_sesinvalids3confex INTO DATA(lo_ex1).
        DATA(lv_error) = |Invalid S3 configuration: { lo_ex1->get_text( ) }|.
        MESSAGE lv_error TYPE 'I'.
        RAISE EXCEPTION lo_ex1.
      CATCH /aws1/cx_rt_generic INTO DATA(lo_ex_generic).
        lv_error = |An error occurred: { lo_ex_generic->get_text( ) }|.
        MESSAGE lv_error TYPE 'I'.
        RAISE EXCEPTION lo_ex_generic.
    ENDTRY.
```
+  For API details, see [CreateReceiptRule](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `CreateReceiptRuleSet`
<a name="ses_CreateReceiptRuleSet_sap-abap_1_topic"></a>

The following code example shows how to use `CreateReceiptRuleSet`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ses#code-examples).

```
    TRY.
        lo_ses->createreceiptruleset( iv_rulesetname = iv_rule_set_name ).
        MESSAGE 'Receipt rule set created successfully' TYPE 'I'.
      CATCH /aws1/cx_sesalreadyexistsex INTO DATA(lo_ex1).
        DATA(lv_error) = |Rule set already exists: { lo_ex1->get_text( ) }|.
        MESSAGE lv_error TYPE 'I'.
        RAISE EXCEPTION lo_ex1.
      CATCH /aws1/cx_rt_generic INTO DATA(lo_ex_generic).
        lv_error = |An error occurred: { lo_ex_generic->get_text( ) }|.
        MESSAGE lv_error TYPE 'I'.
        RAISE EXCEPTION lo_ex_generic.
    ENDTRY.
```
+  For API details, see [CreateReceiptRuleSet](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `CreateTemplate`
<a name="ses_CreateTemplate_sap-abap_1_topic"></a>

The following code example shows how to use `CreateTemplate`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ses#code-examples).

```
    DATA(lo_template) = NEW /aws1/cl_sestemplate(
      iv_templatename = iv_name
      iv_subjectpart = iv_subject
      iv_textpart = iv_text
      iv_htmlpart = iv_html
    ).

    TRY.
        lo_ses->createtemplate( io_template = lo_template ).
        MESSAGE 'Template created successfully' TYPE 'I'.
      CATCH /aws1/cx_sesalreadyexistsex INTO DATA(lo_ex1).
        DATA(lv_error) = |Template already exists: { lo_ex1->get_text( ) }|.
        MESSAGE lv_error TYPE 'I'.
        RAISE EXCEPTION lo_ex1.
      CATCH /aws1/cx_sesinvalidtemplateex INTO DATA(lo_ex2).
        lv_error = |Invalid template: { lo_ex2->get_text( ) }|.
        MESSAGE lv_error TYPE 'I'.
        RAISE EXCEPTION lo_ex2.
      CATCH /aws1/cx_rt_generic INTO DATA(lo_ex_generic).
        lv_error = |An error occurred: { lo_ex_generic->get_text( ) }|.
        MESSAGE lv_error TYPE 'I'.
        RAISE EXCEPTION lo_ex_generic.
    ENDTRY.
```
+  For API details, see [CreateTemplate](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `DeleteIdentity`
<a name="ses_DeleteIdentity_sap-abap_1_topic"></a>

The following code example shows how to use `DeleteIdentity`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ses#code-examples).

```
    TRY.
        lo_ses->deleteidentity( iv_identity = iv_identity ).
        MESSAGE 'Identity deleted successfully' TYPE 'I'.
      CATCH /aws1/cx_rt_generic INTO DATA(lo_ex).
        DATA(lv_error) = |An error occurred: { lo_ex->get_text( ) }|.
        MESSAGE lv_error TYPE 'I'.
        RAISE EXCEPTION lo_ex.
    ENDTRY.
```
+  For API details, see [DeleteIdentity](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `DeleteReceiptFilter`
<a name="ses_DeleteReceiptFilter_sap-abap_1_topic"></a>

The following code example shows how to use `DeleteReceiptFilter`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ses#code-examples).

```
    TRY.
        lo_ses->deletereceiptfilter( iv_filtername = iv_filter_name ).
        MESSAGE 'Receipt filter deleted successfully' TYPE 'I'.
      CATCH /aws1/cx_rt_generic INTO DATA(lo_ex).
        DATA(lv_error) = |An error occurred: { lo_ex->get_text( ) }|.
        MESSAGE lv_error TYPE 'I'.
        RAISE EXCEPTION lo_ex.
    ENDTRY.
```
+  For API details, see [DeleteReceiptFilter](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `DeleteReceiptRule`
<a name="ses_DeleteReceiptRule_sap-abap_1_topic"></a>

The following code example shows how to use `DeleteReceiptRule`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ses#code-examples).

```
    TRY.
        lo_ses->deletereceiptrule(
          iv_rulesetname = iv_rule_set_name
          iv_rulename = iv_rule_name
        ).
        MESSAGE 'Receipt rule deleted successfully' TYPE 'I'.
      CATCH /aws1/cx_sesrulesetdoesnotexex INTO DATA(lo_ex1).
        DATA(lv_error) = |Rule set does not exist: { lo_ex1->get_text( ) }|.
        MESSAGE lv_error TYPE 'I'.
        RAISE EXCEPTION lo_ex1.
      CATCH /aws1/cx_rt_generic INTO DATA(lo_ex_generic).
        lv_error = |An error occurred: { lo_ex_generic->get_text( ) }|.
        MESSAGE lv_error TYPE 'I'.
        RAISE EXCEPTION lo_ex_generic.
    ENDTRY.
```
+  For API details, see [DeleteReceiptRule](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `DeleteReceiptRuleSet`
<a name="ses_DeleteReceiptRuleSet_sap-abap_1_topic"></a>

The following code example shows how to use `DeleteReceiptRuleSet`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ses#code-examples).

```
    TRY.
        lo_ses->deletereceiptruleset( iv_rulesetname = iv_rule_set_name ).
        MESSAGE 'Receipt rule set deleted successfully' TYPE 'I'.
      CATCH /aws1/cx_sescannotdeleteex INTO DATA(lo_ex1).
        DATA(lv_error) = |Cannot delete rule set: { lo_ex1->get_text( ) }|.
        MESSAGE lv_error TYPE 'I'.
        RAISE EXCEPTION lo_ex1.
      CATCH /aws1/cx_rt_generic INTO DATA(lo_ex_generic).
        lv_error = |An error occurred: { lo_ex_generic->get_text( ) }|.
        MESSAGE lv_error TYPE 'I'.
        RAISE EXCEPTION lo_ex_generic.
    ENDTRY.
```
+  For API details, see [DeleteReceiptRuleSet](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `DeleteTemplate`
<a name="ses_DeleteTemplate_sap-abap_1_topic"></a>

The following code example shows how to use `DeleteTemplate`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ses#code-examples).

```
    TRY.
        lo_ses->deletetemplate( iv_templatename = iv_template_name ).
        MESSAGE 'Template deleted successfully' TYPE 'I'.
      CATCH /aws1/cx_rt_generic INTO DATA(lo_ex).
        DATA(lv_error) = |An error occurred: { lo_ex->get_text( ) }|.
        MESSAGE lv_error TYPE 'I'.
        RAISE EXCEPTION lo_ex.
    ENDTRY.
```
+  For API details, see [DeleteTemplate](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `DescribeReceiptRuleSet`
<a name="ses_DescribeReceiptRuleSet_sap-abap_1_topic"></a>

The following code example shows how to use `DescribeReceiptRuleSet`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ses#code-examples).

```
    TRY.
        oo_result = lo_ses->describereceiptruleset(
          iv_rulesetname = iv_rule_set_name
        ).
        MESSAGE 'Receipt rule set described successfully' TYPE 'I'.
      CATCH /aws1/cx_sesrulesetdoesnotexex INTO DATA(lo_ex1).
        DATA(lv_error) = |Rule set does not exist: { lo_ex1->get_text( ) }|.
        MESSAGE lv_error TYPE 'I'.
        RAISE EXCEPTION lo_ex1.
      CATCH /aws1/cx_rt_generic INTO DATA(lo_ex_generic).
        lv_error = |An error occurred: { lo_ex_generic->get_text( ) }|.
        MESSAGE lv_error TYPE 'I'.
        RAISE EXCEPTION lo_ex_generic.
    ENDTRY.
```
+  For API details, see [DescribeReceiptRuleSet](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `GetIdentityVerificationAttributes`
<a name="ses_GetIdentityVerificationAttributes_sap-abap_1_topic"></a>

The following code example shows how to use `GetIdentityVerificationAttributes`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ses#code-examples).

```
    DATA lt_identities TYPE /aws1/cl_sesidentitylist_w=>tt_identitylist.
    APPEND NEW /aws1/cl_sesidentitylist_w( iv_value = iv_identity ) TO lt_identities.

    TRY.
        DATA(lo_result) = lo_ses->getidentityverificationattrs(
          it_identities = lt_identities
        ).

        DATA(lt_attrs) = lo_result->get_verificationattributes( ).
        IF lt_attrs IS NOT INITIAL.
          LOOP AT lt_attrs ASSIGNING FIELD-SYMBOL(<ls_attr>).
            ov_status = <ls_attr>-value->get_verificationstatus( ).
            EXIT.
          ENDLOOP.
        ELSE.
          ov_status = 'NotFound'.
        ENDIF.
      CATCH /aws1/cx_rt_generic INTO DATA(lo_ex).
        DATA(lv_error) = |An error occurred: { lo_ex->get_text( ) }|.
        MESSAGE lv_error TYPE 'I'.
        RAISE EXCEPTION lo_ex.
    ENDTRY.
```
+  For API details, see [GetIdentityVerificationAttributes](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `GetTemplate`
<a name="ses_GetTemplate_sap-abap_1_topic"></a>

The following code example shows how to use `GetTemplate`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ses#code-examples).

```
    TRY.
        DATA(lo_result) = lo_ses->gettemplate( iv_templatename = iv_template_name ).
        oo_template = lo_result->get_template( ).
        MESSAGE 'Template retrieved successfully' TYPE 'I'.
      CATCH /aws1/cx_sestmpldoesnotexistex INTO DATA(lo_ex1).
        DATA(lv_error) = |Template does not exist: { lo_ex1->get_text( ) }|.
        MESSAGE lv_error TYPE 'I'.
        RAISE EXCEPTION lo_ex1.
      CATCH /aws1/cx_rt_generic INTO DATA(lo_ex_generic).
        lv_error = |An error occurred: { lo_ex_generic->get_text( ) }|.
        MESSAGE lv_error TYPE 'I'.
        RAISE EXCEPTION lo_ex_generic.
    ENDTRY.
```
+  For API details, see [GetTemplate](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `ListIdentities`
<a name="ses_ListIdentities_sap-abap_1_topic"></a>

The following code example shows how to use `ListIdentities`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ses#code-examples).

```
    TRY.
        DATA(lo_result) = lo_ses->listidentities(
          iv_identitytype = iv_identity_type
          iv_maxitems = iv_max_items
        ).
        ot_identities = lo_result->get_identities( ).
        MESSAGE 'Identities retrieved successfully' TYPE 'I'.
      CATCH /aws1/cx_rt_generic INTO DATA(lo_ex).
        DATA(lv_error) = |An error occurred: { lo_ex->get_text( ) }|.
        MESSAGE lv_error TYPE 'I'.
        RAISE EXCEPTION lo_ex.
    ENDTRY.
```
+  For API details, see [ListIdentities](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `ListReceiptFilters`
<a name="ses_ListReceiptFilters_sap-abap_1_topic"></a>

The following code example shows how to use `ListReceiptFilters`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ses#code-examples).

```
    TRY.
        DATA(lo_result) = lo_ses->listreceiptfilters( ).
        ot_filters = lo_result->get_filters( ).
        MESSAGE 'Receipt filters retrieved successfully' TYPE 'I'.
      CATCH /aws1/cx_rt_generic INTO DATA(lo_ex).
        DATA(lv_error) = |An error occurred: { lo_ex->get_text( ) }|.
        MESSAGE lv_error TYPE 'I'.
        RAISE EXCEPTION lo_ex.
    ENDTRY.
```
+  For API details, see [ListReceiptFilters](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `ListTemplates`
<a name="ses_ListTemplates_sap-abap_1_topic"></a>

The following code example shows how to use `ListTemplates`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ses#code-examples).

```
    TRY.
        DATA(lo_result) = lo_ses->listtemplates( iv_maxitems = iv_max_items ).
        ot_templates = lo_result->get_templatesmetadata( ).
        MESSAGE 'Templates retrieved successfully' TYPE 'I'.
      CATCH /aws1/cx_rt_generic INTO DATA(lo_ex).
        DATA(lv_error) = |An error occurred: { lo_ex->get_text( ) }|.
        MESSAGE lv_error TYPE 'I'.
        RAISE EXCEPTION lo_ex.
    ENDTRY.
```
+  For API details, see [ListTemplates](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `SendEmail`
<a name="ses_SendEmail_sap-abap_1_topic"></a>

The following code example shows how to use `SendEmail`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ses#code-examples).

```
    " Create message object
    DATA(lo_subject) = NEW /aws1/cl_sescontent( iv_data = iv_subject ).
    DATA(lo_text_body) = NEW /aws1/cl_sescontent( iv_data = iv_text ).
    DATA(lo_html_body) = NEW /aws1/cl_sescontent( iv_data = iv_html ).
    DATA(lo_body) = NEW /aws1/cl_sesbody(
      io_text = lo_text_body
      io_html = lo_html_body
    ).
    DATA(lo_message) = NEW /aws1/cl_sesmessage(
      io_subject = lo_subject
      io_body = lo_body
    ).

    TRY.
        " Send email
        DATA(lo_result) = lo_ses->sendemail(
          iv_source = iv_source
          io_destination = io_destination
          io_message = lo_message
          it_replytoaddresses = it_reply_tos
        ).
        ov_msg_id = lo_result->get_messageid( ).
        MESSAGE 'Email sent successfully' TYPE 'I'.
      CATCH /aws1/cx_sesacctsendingpause00 INTO DATA(lo_ex1).
        DATA(lv_error) = |Account sending paused: { lo_ex1->get_text( ) }|.
        MESSAGE lv_error TYPE 'I'.
        RAISE EXCEPTION lo_ex1.
      CATCH /aws1/cx_sesmessagerejected INTO DATA(lo_ex2).
        lv_error = |Message rejected: { lo_ex2->get_text( ) }|.
        MESSAGE lv_error TYPE 'I'.
        RAISE EXCEPTION lo_ex2.
      CATCH /aws1/cx_rt_generic INTO DATA(lo_ex_generic).
        lv_error = |An error occurred: { lo_ex_generic->get_text( ) }|.
        MESSAGE lv_error TYPE 'I'.
        RAISE EXCEPTION lo_ex_generic.
    ENDTRY.
```
+  For API details, see [SendEmail](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `SendTemplatedEmail`
<a name="ses_SendTemplatedEmail_sap-abap_1_topic"></a>

The following code example shows how to use `SendTemplatedEmail`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ses#code-examples).

```
    TRY.
        " Send templated email
        DATA(lo_result) = lo_ses->sendtemplatedemail(
          iv_source = iv_source
          io_destination = io_destination
          iv_template = iv_template_name
          iv_templatedata = iv_template_data
          it_replytoaddresses = it_reply_tos
        ).
        ov_msg_id = lo_result->get_messageid( ).
        MESSAGE 'Templated email sent successfully' TYPE 'I'.
      CATCH /aws1/cx_sestmpldoesnotexistex INTO DATA(lo_ex1).
        DATA(lv_error) = |Template does not exist: { lo_ex1->get_text( ) }|.
        MESSAGE lv_error TYPE 'I'.
        RAISE EXCEPTION lo_ex1.
      CATCH /aws1/cx_rt_generic INTO DATA(lo_ex_generic).
        lv_error = |An error occurred: { lo_ex_generic->get_text( ) }|.
        MESSAGE lv_error TYPE 'I'.
        RAISE EXCEPTION lo_ex_generic.
    ENDTRY.
```
+  For API details, see [SendTemplatedEmail](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `UpdateTemplate`
<a name="ses_UpdateTemplate_sap-abap_1_topic"></a>

The following code example shows how to use `UpdateTemplate`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ses#code-examples).

```
    DATA(lo_template) = NEW /aws1/cl_sestemplate(
      iv_templatename = iv_name
      iv_subjectpart = iv_subject
      iv_textpart = iv_text
      iv_htmlpart = iv_html
    ).

    TRY.
        lo_ses->updatetemplate( io_template = lo_template ).
        MESSAGE 'Template updated successfully' TYPE 'I'.
      CATCH /aws1/cx_sestmpldoesnotexistex INTO DATA(lo_ex1).
        DATA(lv_error) = |Template does not exist: { lo_ex1->get_text( ) }|.
        MESSAGE lv_error TYPE 'I'.
        RAISE EXCEPTION lo_ex1.
      CATCH /aws1/cx_sesinvalidtemplateex INTO DATA(lo_ex2).
        lv_error = |Invalid template: { lo_ex2->get_text( ) }|.
        MESSAGE lv_error TYPE 'I'.
        RAISE EXCEPTION lo_ex2.
      CATCH /aws1/cx_rt_generic INTO DATA(lo_ex_generic).
        lv_error = |An error occurred: { lo_ex_generic->get_text( ) }|.
        MESSAGE lv_error TYPE 'I'.
        RAISE EXCEPTION lo_ex_generic.
    ENDTRY.
```
+  For API details, see [UpdateTemplate](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `VerifyDomainIdentity`
<a name="ses_VerifyDomainIdentity_sap-abap_1_topic"></a>

The following code example shows how to use `VerifyDomainIdentity`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ses#code-examples).

```
    TRY.
        DATA(lo_result) = lo_ses->verifydomainidentity( iv_domain = iv_domain_name ).
        ov_token = lo_result->get_verificationtoken( ).
        MESSAGE 'Domain verification initiated' TYPE 'I'.
      CATCH /aws1/cx_rt_generic INTO DATA(lo_ex).
        DATA(lv_error) = |An error occurred: { lo_ex->get_text( ) }|.
        MESSAGE lv_error TYPE 'I'.
        RAISE EXCEPTION lo_ex.
    ENDTRY.
```
+  For API details, see [VerifyDomainIdentity](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `VerifyEmailIdentity`
<a name="ses_VerifyEmailIdentity_sap-abap_1_topic"></a>

The following code example shows how to use `VerifyEmailIdentity`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ses#code-examples).

```
    TRY.
        lo_ses->verifyemailidentity( iv_emailaddress = iv_email_address ).
        MESSAGE 'Email verification initiated' TYPE 'I'.
      CATCH /aws1/cx_rt_generic INTO DATA(lo_ex).
        DATA(lv_error) = |An error occurred: { lo_ex->get_text( ) }|.
        MESSAGE lv_error TYPE 'I'.
        RAISE EXCEPTION lo_ex.
    ENDTRY.
```
+  For API details, see [VerifyEmailIdentity](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.
