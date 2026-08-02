---
source_url: https://docs.aws.amazon.com/online-register/latest/data-formats/amazonlex.html
---

# Data retrieval APIs for Amazon Lex
<a name="amazonlex"></a>

Amazon Lex provides the following APIs for data retrieval.

****

| Actions | Description | Access level |
| --- | --- | --- |
| <a name="lex-GetBot"></a>[https://docs.aws.amazon.com/lex/latest/dg/API_GetBot.html](https://docs.aws.amazon.com/lex/latest/dg/API_GetBot.html) | Returns information for a specific bot. In addition to the bot name, the bot version or alias is required | Read |
| <a name="lex-GetBotAlias"></a>[https://docs.aws.amazon.com/lex/latest/dg/API_GetBotAlias.html](https://docs.aws.amazon.com/lex/latest/dg/API_GetBotAlias.html) | Returns information about a Amazon Lex bot alias | Read |
| <a name="lex-GetBotAliases"></a>[https://docs.aws.amazon.com/lex/latest/dg/API_GetBotAliases.html](https://docs.aws.amazon.com/lex/latest/dg/API_GetBotAliases.html) | Returns a list of aliases for a given Amazon Lex bot | List |
| <a name="lex-GetBotChannelAssociation"></a>[https://docs.aws.amazon.com/lex/latest/dg/API_GetBotChannelAssociation.html](https://docs.aws.amazon.com/lex/latest/dg/API_GetBotChannelAssociation.html) | Returns information about the association between a Amazon Lex bot and a messaging platform | Read |
| <a name="lex-GetBotChannelAssociations"></a>[https://docs.aws.amazon.com/lex/latest/dg/API_GetBotChannelAssociations.html](https://docs.aws.amazon.com/lex/latest/dg/API_GetBotChannelAssociations.html) | Returns a list of all of the channels associated with a single bot | List |
| <a name="lex-GetBotVersions"></a>[https://docs.aws.amazon.com/lex/latest/dg/API_GetBotVersions.html](https://docs.aws.amazon.com/lex/latest/dg/API_GetBotVersions.html) | Returns information for all versions of a specific bot | List |
| <a name="lex-GetBots"></a>[https://docs.aws.amazon.com/lex/latest/dg/API_GetBots.html](https://docs.aws.amazon.com/lex/latest/dg/API_GetBots.html) | Returns information for the $LATEST version of all bots, subject to filters provided by the client | List |
| <a name="lex-GetBuiltinIntent"></a>[https://docs.aws.amazon.com/lex/latest/dg/API_GetBuiltinIntent.html](https://docs.aws.amazon.com/lex/latest/dg/API_GetBuiltinIntent.html) | Returns information about a built-in intent | Read |
| <a name="lex-GetBuiltinIntents"></a>[https://docs.aws.amazon.com/lex/latest/dg/API_GetBuiltinIntents.html](https://docs.aws.amazon.com/lex/latest/dg/API_GetBuiltinIntents.html) | Gets a list of built-in intents that meet the specified criteria | Read |
| <a name="lex-GetBuiltinSlotTypes"></a>[https://docs.aws.amazon.com/lex/latest/dg/API_GetBuiltinSlotTypes.html](https://docs.aws.amazon.com/lex/latest/dg/API_GetBuiltinSlotTypes.html) | Gets a list of built-in slot types that meet the specified criteria | Read |
| <a name="lex-GetExport"></a>[https://docs.aws.amazon.com/lex/latest/dg/API_GetExport.html](https://docs.aws.amazon.com/lex/latest/dg/API_GetExport.html) | Exports Amazon Lex Resource in a requested format | Read |
| <a name="lex-GetImport"></a>[https://docs.aws.amazon.com/lex/latest/dg/API_GetImport.html](https://docs.aws.amazon.com/lex/latest/dg/API_GetImport.html) | Gets information about an import job started with StartImport | Read |
| <a name="lex-GetIntent"></a>[https://docs.aws.amazon.com/lex/latest/dg/API_GetIntent.html](https://docs.aws.amazon.com/lex/latest/dg/API_GetIntent.html) | Returns information for a specific intent. In addition to the intent name, you must also specify the intent version | Read |
| <a name="lex-GetIntentVersions"></a>[https://docs.aws.amazon.com/lex/latest/dg/API_GetIntentVersions.html](https://docs.aws.amazon.com/lex/latest/dg/API_GetIntentVersions.html) | Returns information for all versions of a specific intent | List |
| <a name="lex-GetIntents"></a>[https://docs.aws.amazon.com/lex/latest/dg/API_GetIntents.html](https://docs.aws.amazon.com/lex/latest/dg/API_GetIntents.html) | Returns information for the $LATEST version of all intents, subject to filters provided by the client | List |
| <a name="lex-GetMigration"></a>[https://docs.aws.amazon.com/lex/latest/dg/API_GetMigration.html](https://docs.aws.amazon.com/lex/latest/dg/API_GetMigration.html) | View an ongoing or completed migration | Read |
| <a name="lex-GetMigrations"></a>[https://docs.aws.amazon.com/lex/latest/dg/API_GetMigrations.html](https://docs.aws.amazon.com/lex/latest/dg/API_GetMigrations.html) | View list of migrations from Amazon Lex v1 to Amazon Lex v2 | List |
| <a name="lex-GetSession"></a>[https://docs.aws.amazon.com/lex/latest/dg/API_runtime_GetSession.html](https://docs.aws.amazon.com/lex/latest/dg/API_runtime_GetSession.html) | Returns session information for a specified bot, alias, and user ID | Read |
| <a name="lex-GetSlotType"></a>[https://docs.aws.amazon.com/lex/latest/dg/API_GetSlotType.html](https://docs.aws.amazon.com/lex/latest/dg/API_GetSlotType.html) | Returns information about a specific version of a slot type. In addition to specifying the slot type name, you must also specify the slot type version | Read |
| <a name="lex-GetSlotTypeVersions"></a>[https://docs.aws.amazon.com/lex/latest/dg/API_GetSlotTypeVersions.html](https://docs.aws.amazon.com/lex/latest/dg/API_GetSlotTypeVersions.html) | Returns information for all versions of a specific slot type | List |
| <a name="lex-GetSlotTypes"></a>[https://docs.aws.amazon.com/lex/latest/dg/API_GetSlotTypes.html](https://docs.aws.amazon.com/lex/latest/dg/API_GetSlotTypes.html) | Returns information for the $LATEST version of all slot types, subject to filters provided by the client | List |
| <a name="lex-GetUtterancesView"></a>[https://docs.aws.amazon.com/lex/latest/dg/API_GetUtterancesView.html](https://docs.aws.amazon.com/lex/latest/dg/API_GetUtterancesView.html) | Returns a view of aggregate utterance data for versions of a bot for a recent time period | List |
| <a name="lex-ListTagsForResource"></a>[https://docs.aws.amazon.com/lex/latest/dg/API_ListTagsForResource.html](https://docs.aws.amazon.com/lex/latest/dg/API_ListTagsForResource.html) | Lists tags for a Lex resource | Read |
