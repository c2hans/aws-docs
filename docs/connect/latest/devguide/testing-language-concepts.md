---
source_url: https://docs.aws.amazon.com/connect/latest/devguide/testing-language-concepts.html
---

# Connect Customer Testing language concepts
<a name="testing-language-concepts"></a>

The following terms are used in the Testing language.

## Observations
<a name="testing-language-concepts-observations"></a>

Observations represent each complete interaction that includes one observed event expected from the system and many actions to validate or simulate system behaviors.

## Events
<a name="testing-language-concepts-events"></a>

Events represent expected behaviors that would come from the system, such as a prompt, a bot message, or a Lambda call.

## Actions
<a name="testing-language-concepts-actions"></a>

Actions represent what the testing framework should do in response to an event, such as sending DTMF, responding with text, asserting attribute values, or ending the test.

## Actors
<a name="testing-language-concepts-actors"></a>

Actors represent roles to be played in the testing framework. When observing events, actors can be the system or agent, such as a play prompt coming from the system or an agent accepting the call. When simulating actions, actors can be the customer, system, or agent, such as simulating a customer input DTMF or utterance, or simulating a system response from a Lambda function.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
