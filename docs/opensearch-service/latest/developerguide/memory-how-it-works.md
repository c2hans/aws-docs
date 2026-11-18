---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/memory-how-it-works.html
---

# How Amazon OpenSearch Memory works
<a name="memory-how-it-works"></a>

In Amazon OpenSearch Memory, spaces, events, and memories are the core components that you work with. A *space* holds the events that you send and the memories extracted from them. An *event* is content that your agent or application sends to a space, such as a conversation turn, a JSON record, or a document. A *memory* is a fact, summary, or other detail that OpenSearch Memory extracted from events, or that you wrote directly.

This topic describes these components and what happens between writing an event and finding a memory.

**Topics**
+ [Spaces, events, and memories](#memory-how-it-works-core-components)
+ [Actors and sessions](#memory-how-it-works-actors-sessions)
+ [Memory strategies](#memory-how-it-works-strategies)
+ [From event to memory](#memory-how-it-works-lifecycle)
+ [What you see, and when](#memory-how-it-works-consistency)

## Spaces, events, and memories
<a name="memory-how-it-works-core-components"></a>

The following are the basic OpenSearch Memory components:
+ **Spaces** – A space is an AWS resource that stores events and memories. It defines which memory strategies extract memories, how long events and memories are kept, which model extracts memories, and which key encrypts the data. Each space has an ID, such as `sp-02864597b164`, and an ARN. A space is the unit you control access to with IAM.
+ **Events** – An event is content that your agent or application sends to a space with [CreateEvent](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_CreateEvent.html). Each event has one of three kinds of payload:
  + *Conversational* – One or more conversation turns, each with a role (`USER`, `ASSISTANT`, or `SYSTEM`) and text.
  + *Structured data* – A JSON object, such as the result of a deployment that an agent should remember.
  + *Blob* – A document in Amazon S3, such as a PDF, PNG, or JPEG file.

  OpenSearch Memory stores the event as you sent it and returns it unchanged from [GetEvent](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_GetEvent.html). A space keeps each event for the number of days in its `eventExpiryDays` setting.
+ **Memories** – A memory is a piece of text that OpenSearch Memory extracted from one or more events, or that you wrote with [CreateMemory](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_CreateMemory.html). Each memory has a type that matches the strategy that produced it (`SEMANTIC`, `SUMMARY`, or `CUSTOM`), the IDs of the events it came from, the actor and session it belongs to, timestamps, and any metadata tags you attached. A space keeps each memory for the number of days in its `memoryExpiryDays` setting, or forever if you don't set one.

The following example shows a conversational event and two memories that a space with a `SEMANTIC` strategy and a `SUMMARY` strategy might extract from it.

```
Event (conversational)
  actorId:   user-123
  sessionId: session-001
  messages:
    USER:      "I'm vegetarian, so please suggest meat-free recipes."
    ASSISTANT: "Here are three meat-free recipes for this week."

Memory (SEMANTIC, strategy "user-facts")
  content: "The user is vegetarian."
  sourceEventIds: [ev-8f3a2c1d9b7e]

Memory (SUMMARY, strategy "summary_1")
  content: "The user asked for vegetarian recipes and received three meat-free options for the week."
  sourceEventIds: [ev-8f3a2c1d9b7e]
```

Note the following about this example:
+ The event is stored verbatim. The memories are new text that the extraction model wrote.
+ Each memory records which events it came from, so your application can show its evidence.
+ The two strategies read the same event and produced different kinds of memory.

## Actors and sessions
<a name="memory-how-it-works-actors-sessions"></a>

Every event and memory belongs to an *actor* and a *session*.
+ **Actor** – The user that the content is about, identified by the `actorId` that you choose. For example, each end user of a chat application is an actor. Every search covers exactly one actor. Memories about one actor are never returned when you search another.
+ **Session** – One conversation, identified by a `sessionId`. Send every event of one conversation with the same session ID. `SUMMARY` strategies summarize a session, and extraction batches the turns of a session together, so a conversation split across session IDs produces weaker memories. If you omit the session ID, OpenSearch Memory generates one and returns it.

You choose both IDs. Use stable, non-sensitive values such as your own user and conversation identifiers.

## Memory strategies
<a name="memory-how-it-works-strategies"></a>

A *memory strategy* defines one kind of memory that a space extracts. A space can have up to 10 strategies, and each one extracts from the same events independently. OpenSearch Memory provides three strategy types:
+ `SEMANTIC` – Extracts facts and preferences, such as "prefers window seats."
+ `SUMMARY` – Summarizes each session and keeps the summary up to date as the session continues.
+ `CUSTOM` – Extracts what your own prompt describes, such as "every order ID and its status."

A space with no strategies stores events and lets you search them, but extracts no memories. You can add strategies to a space at any time with [UpdateSpace](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_UpdateSpace.html). For more information, see [Memory strategies in Amazon OpenSearch Memory](memory-strategies.md).

## From event to memory
<a name="memory-how-it-works-lifecycle"></a>

OpenSearch Memory separates storing an event from extracting memories. The following steps describe what happens when your agent sends a conversation.

1. **You send an event.** Your agent calls `CreateEvent` with the actor, the session, and the turns. The call returns as soon as the event is stored. The event is immediately available to `GetEvent` and [ListEvents](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_ListEvents.html).

1. **Turns accumulate.** Each strategy collects the session's turns until one of its *extraction triggers* fires: a number of messages, a number of tokens, or a period of silence (the *idle timeout*). The idle timeout is what extracts the end of a conversation that simply stops. For more information, see [Extraction triggers](memory-strategies.md#memory-strategies-triggers).

1. **Memories are extracted.** When a trigger fires, the strategy sends the accumulated turns to the extraction model with its instructions and receives candidate memories.

1. **Memories are consolidated.** For a strategy with consolidation on, OpenSearch Memory compares each candidate with the similar memories it already holds for that actor and strategy. It then adds the candidate as a new memory, updates an existing memory with the newer information, or discards the candidate as a duplicate. For more information, see [Consolidation](memory-strategies.md#memory-strategies-consolidation).

1. **Memories become searchable.** The resulting memories are indexed. [SearchMemories](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_SearchMemories.html) now returns them, ranked by relevance to your query.

Events with structured data follow the same path. For a blob event, OpenSearch Memory first reads the document from Amazon S3 and splits it into passages, which are then extracted like conversation turns and are also searchable with [SearchEvents](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_SearchEvents.html).

## What you see, and when
<a name="memory-how-it-works-consistency"></a>

Because extraction runs after `CreateEvent` returns, different operations reflect a new event at different times.

| Operation | Reflects a new event or memory |
| --- | --- |
| GetEvent, [BatchGetEvent](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_BatchGetEvent.html), ListEvents | As soon as CreateEvent returns |
| SearchEvents | Shortly after CreateEvent returns, when the event's content is indexed |
| SearchMemories, [ListMemories](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_ListMemories.html), [GetMemory](https://docs.aws.amazon.com/opensearch-service/latest/MemoryAPIReference/API_GetMemory.html) (extracted memories) | After a strategy's extraction trigger fires and the memories are indexed. With default settings, this is within a minute after the conversation goes quiet |
| GetMemory, ListMemories, SearchMemories (memories written with CreateMemory) | Shortly after CreateMemory returns, when the memory is indexed |

Deletes behave the same way in reverse: a deleted event or memory can still appear in search results for a short time after the delete call returns.

If your application needs a memory to be searchable before it continues, poll `GetMemory` with backoff until the memory is returned. If you need memories sooner after a conversation, lower the strategy's `extractEveryNMessages` or `idleTimeoutSeconds`. For more information, see [Memory strategies in Amazon OpenSearch Memory](memory-strategies.md).
