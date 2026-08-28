---
source_url: https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/sap-abap_bedrock-agent-runtime_code_examples.html
---

# Amazon Bedrock Agents Runtime examples using SDK for SAP ABAP
<a name="sap-abap_bedrock-agent-runtime_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for SAP ABAP with Amazon Bedrock Agents Runtime.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `InvokeAgent`
<a name="bedrock-agent-runtime_InvokeAgent_sap-abap_topic"></a>

The following code example shows how to use `InvokeAgent`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/bdz#code-examples).

```
    DATA(lo_result) = lo_bdz->invokeagent(
      iv_agentid      = iv_agentid
        iv_agentaliasid = iv_agentaliasid
        iv_enabletrace  = abap_true
        iv_sessionid    = CONV #( cl_system_uuid=>create_uuid_c26_static( ) )
        iv_inputtext    = |Let's play "rock, paper, scissors".  I choose rock.| ).
    DATA(lo_stream) = lo_result->get_completion( ).
    TRY.
        " loop while there are still events in the stream
        WHILE lo_stream->/aws1/if_rt_stream_reader~data_available( ) = abap_true.
          DATA(lo_evt) = lo_stream->read( ).
          " each /AWS1/CL_BDZRESPONSESTREAM_EV event contains exactly one member
          " all others are INITIAL.  For each event, process the non-initial
          " member if desired
          IF lo_evt->get_chunk( ) IS NOT INITIAL.
            " Process a Chunk event
            DATA(lv_xstr) = lo_evt->get_chunk( )->get_bytes( ).
            DATA(lv_answer) = /aws1/cl_rt_util=>xstring_to_string( lv_xstr ).
            " the answer says something like "I chose paper, so you lost"
          ELSEIF lo_evt->get_files( ) IS NOT INITIAL.
            " process a Files event if desired
          ELSEIF lo_evt->get_returncontrol( ) IS NOT INITIAL.
            " process a ReturnControl event if desired
          ELSEIF lo_evt->get_trace( ) IS NOT INITIAL.
            " process a Trace event if desired
          ENDIF.
        ENDWHILE.
        " the stream of events can possibly contain an exception
        " which will be raised to break the loop
        " catch /AWS1/CX_BDZACCESSDENIEDEX.
        " catch /AWS1/CX_BDZINTERNALSERVEREX.
        " catch /AWS1/CX_BDZMODELNOTREADYEX.
        " catch /AWS1/CX_BDZVALIDATIONEX.
        " catch /AWS1/CX_BDZTHROTTLINGEX.
        " catch /AWS1/CX_BDZDEPENDENCYFAILEDEX.
        " catch /AWS1/CX_BDZBADGATEWAYEX.
        " catch /AWS1/CX_BDZRESOURCENOTFOUNDEX.
        " catch /AWS1/CX_BDZSERVICEQUOTAEXCDEX.
        " catch /AWS1/CX_BDZCONFLICTEXCEPTION.
    ENDTRY.
```
+  For API details, see [InvokeAgent](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for SAP ABAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-sapabap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
