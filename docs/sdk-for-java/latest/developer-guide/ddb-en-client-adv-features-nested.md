---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/ddb-en-client-adv-features-nested.html
---

# Work with attributes that are beans, maps, lists and sets
<a name="ddb-en-client-adv-features-nested"></a>

A bean definition, such as the `Person` class shown below, might define properties (or attributes) that refer to types with additional attributes. For instance, in the `Person` class, `mainAddress` is a property that refers to an `Address` bean that defines additional value attributes. `addresses` refers to a Java Map, whose elements refer to `Address` beans. These complex types can be thought of a containers of simple attributes that you use for their data value in the context of DynamoDB.

DynamoDB refers to the value properties of nested elements, such as maps, lists, or beans, as *nested attributes*. The [Amazon DynamoDB Developer Guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.NamingRulesDataTypes.html#HowItWorks.DataTypes) refers to the saved form of a Java map, list or bean as a *document type*. Simple attributes that you use for their data value in Java are referred to as *scalar types* in DynamoDB. Sets, which contains multiple scalar elements of the same type, and referred to as *set types*.

It is important to know that the DynamoDB Enhanced Client API converts a property that is bean to a DynamoDB map document type when it is save.

## `Person` class
<a name="ddb-en-client-adv-features-nested-person"></a>

```
@DynamoDbBean
public class Person {
    private Integer id;
    private String firstName;
    private String lastName;
    private Integer age;
    private Address mainAddress;
    private Map<String, Address> addresses;
    private List<PhoneNumber> phoneNumbers;
    private Set<String> hobbies;

    @DynamoDbPartitionKey
    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getFirstName() {
        return firstName;
    }

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public String getLastName() {
        return lastName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public Integer getAge() {
        return age;
    }

    public void setAge(Integer age) {
        this.age = age;
    }

    public Address getMainAddress() {
        return mainAddress;
    }

    public void setMainAddress(Address mainAddress) {
        this.mainAddress = mainAddress;
    }

    public Map<String, Address> getAddresses() {
        return addresses;
    }

    public void setAddresses(Map<String, Address> addresses) {
        this.addresses = addresses;
    }

    public List<PhoneNumber> getPhoneNumbers() {
        return phoneNumbers;
    }

    public void setPhoneNumbers(List<PhoneNumber> phoneNumbers) {
        this.phoneNumbers = phoneNumbers;
    }

    public Set<String> getHobbies() {
        return hobbies;
    }

    public void setHobbies(Set<String> hobbies) {
        this.hobbies = hobbies;
    }

    @Override
    public String toString() {
        return "Person{" +
               "addresses=" + addresses +
               ", id=" + id +
               ", firstName='" + firstName + '\'' +
               ", lastName='" + lastName + '\'' +
               ", age=" + age +
               ", mainAddress=" + mainAddress +
               ", phoneNumbers=" + phoneNumbers +
               ", hobbies=" + hobbies +
               '}';
    }
}
```

## `Address` class
<a name="ddb-en-client-adv-features-nested-address"></a>

```
@DynamoDbBean
public class Address {
    private String street;
    private String city;
    private String state;
    private String zipCode;

    public Address() {
    }

    public String getStreet() {
        return this.street;
    }

    public String getCity() {
        return this.city;
    }

    public String getState() {
        return this.state;
    }

    public String getZipCode() {
        return this.zipCode;
    }

    public void setStreet(String street) {
        this.street = street;
    }

    public void setCity(String city) {
        this.city = city;
    }

    public void setState(String state) {
        this.state = state;
    }

    public void setZipCode(String zipCode) {
        this.zipCode = zipCode;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Address address = (Address) o;
        return Objects.equals(street, address.street) && Objects.equals(city, address.city) && Objects.equals(state, address.state) && Objects.equals(zipCode, address.zipCode);
    }

    @Override
    public int hashCode() {
        return Objects.hash(street, city, state, zipCode);
    }

    @Override
    public String toString() {
        return "Address{" +
                "street='" + street + '\'' +
                ", city='" + city + '\'' +
                ", state='" + state + '\'' +
                ", zipCode='" + zipCode + '\'' +
                '}';
    }
}
```

## `PhoneNumber` class
<a name="ddb-en-client-adv-features-nested-phonenumber"></a>

```
@DynamoDbBean
public class PhoneNumber {
    String type;
    String number;

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public String getNumber() {
        return number;
    }

    public void setNumber(String number) {
        this.number = number;
    }

    @Override
    public String toString() {
        return "PhoneNumber{" +
                "type='" + type + '\'' +
                ", number='" + number + '\'' +
                '}';
    }
}
```

## Save complex types
<a name="ddb-en-client-adv-features-nested-mapping"></a>

### Use annotated data classes
<a name="ddb-en-client-adv-features-nested-map-anno"></a>

You save nested attributes for custom classes by simply annotating them. The `Address` class and `PhoneNumber` class shown previously are annotated with only the `@DynamoDbBean` annotation. When the DynamoDB Enhanced Client API builds the table schema for the `Person` class with the following snippet, the API discovers the use of the `Address` and `PhoneNumber` classes and builds the corresponding mappings to work with DynamoDB.

```
TableSchema<Person> personTableSchema = TableSchema.fromBean(Person.class);
```

### Use abstract schemas with builders
<a name="ddb-en-client-adv-features-nested-map-builder"></a>

The alternative approach is to use static table schema builders for each nested bean class as shown in the following code.

The table schemas for the `Address` and `PhoneNumber` classes are abstract in the sense that they cannot be used with a DynamoDB table. This is because they lack definitions for the primary key. They are used, however, as nested schemas in the table schema for the `Person` class.

After comment lines 1 and 2 in the definition of `PERSON_TABLE_SCHEMA`, you see the code that uses the abstract table schemas. The use of `documentOf` in the `EnhanceType.documentOf(...)` method does not indicate that the method returns an `EnhancedDocument` type of the Enhanced Document API. The `documentOf(...)` method in this context returns an object that knows how to map its class argument to and from DynamoDB table attributes by using the table schema argument.

#### Static schema code
<a name="ddb-en-client-adv-features-nested-map-builder-code"></a>

```
    // Abstract table schema that cannot be used to work with a DynamoDB table,
    // but can be used as a nested schema.
    public static final TableSchema<Address> TABLE_SCHEMA_ADDRESS = TableSchema.builder(Address.class)
        .newItemSupplier(Address::new)
        .addAttribute(String.class, a -> a.name("street")
            .getter(Address::getStreet)
            .setter(Address::setStreet))
        .addAttribute(String.class, a -> a.name("city")
            .getter(Address::getCity)
            .setter(Address::setCity))
        .addAttribute(String.class, a -> a.name("zipcode")
            .getter(Address::getZipCode)
            .setter(Address::setZipCode))
        .addAttribute(String.class, a -> a.name("state")
            .getter(Address::getState)
            .setter(Address::setState))
        .build();

    // Abstract table schema that cannot be used to work with a DynamoDB table,
    // but can be used as a nested schema.
    public static final TableSchema<PhoneNumber> TABLE_SCHEMA_PHONENUMBER = TableSchema.builder(PhoneNumber.class)
        .newItemSupplier(PhoneNumber::new)
        .addAttribute(String.class, a -> a.name("type")
            .getter(PhoneNumber::getType)
            .setter(PhoneNumber::setType))
        .addAttribute(String.class, a -> a.name("number")
            .getter(PhoneNumber::getNumber)
            .setter(PhoneNumber::setNumber))
        .build();

    // A static table schema that can be used with a DynamoDB table.
    // The table schema contains two nested schemas that are used to perform mapping to/from DynamoDB.
    public static final TableSchema<Person> PERSON_TABLE_SCHEMA =
        TableSchema.builder(Person.class)
            .newItemSupplier(Person::new)
            .addAttribute(Integer.class, a -> a.name("id")
                .getter(Person::getId)
                .setter(Person::setId)
                .addTag(StaticAttributeTags.primaryPartitionKey()))
            .addAttribute(String.class, a -> a.name("firstName")
                .getter(Person::getFirstName)
                .setter(Person::setFirstName))
            .addAttribute(String.class, a -> a.name("lastName")
                .getter(Person::getLastName)
                .setter(Person::setLastName))
            .addAttribute(Integer.class, a -> a.name("age")
                .getter(Person::getAge)
                .setter(Person::setAge))
            .addAttribute(EnhancedType.documentOf(Address.class, TABLE_SCHEMA_ADDRESS), a -> a.name("mainAddress")
                .getter(Person::getMainAddress)
                .setter(Person::setMainAddress))
            .addAttribute(EnhancedType.listOf(String.class), a -> a.name("hobbies")
                .getter(Person::getHobbies)
                .setter(Person::setHobbies))
            .addAttribute(EnhancedType.mapOf(
                EnhancedType.of(String.class),
                // 1. Use mapping functionality of the Address table schema.
                EnhancedType.documentOf(Address.class, TABLE_SCHEMA_ADDRESS)), a -> a.name("addresses")
                .getter(Person::getAddresses)
                .setter(Person::setAddresses))
            .addAttribute(EnhancedType.listOf(
                // 2. Use mapping functionality of the PhoneNumber table schema.
                EnhancedType.documentOf(PhoneNumber.class, TABLE_SCHEMA_PHONENUMBER)), a -> a.name("phoneNumbers")
                .getter(Person::getPhoneNumbers)
                .setter(Person::setPhoneNumbers))
            .build();
```

## Project attributes of complex types
<a name="ddb-en-client-adv-features-nested-projection"></a>

For `query()` and `scan()` methods, you can specify which attributes you want to be returned in the results by using method calls such as `addNestedAttributeToProject()` and `attributesToProject()`. The DynamoDB Enhanced Client API converts the Java method call parameters into [projection expressions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.ProjectionExpressions.html) before the request is sent.

The following example populates the `Person` table with two items, then performs three scan operations.

The first scan accesses all items in the table in order to compare the results to the other scan operations.

The second scan uses the [https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/enhanced/dynamodb/model/ScanEnhancedRequest.Builder.html#addNestedAttributeToProject(software.amazon.awssdk.enhanced.dynamodb.NestedAttributeName)](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/enhanced/dynamodb/model/ScanEnhancedRequest.Builder.html#addNestedAttributeToProject(software.amazon.awssdk.enhanced.dynamodb.NestedAttributeName)) builder method to return only the `street` attribute value.

The third scan operation uses the [https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/enhanced/dynamodb/model/ScanEnhancedRequest.Builder.html#attributesToProject(java.lang.String...)](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/enhanced/dynamodb/model/ScanEnhancedRequest.Builder.html#attributesToProject(java.lang.String...)) builder method to return the data for the first-level attribute, `hobbies`. The attribute type of `hobbies` is a list. To access individual list items, perform a `get()` operation on the list.

```
        personDynamoDbTable = getDynamoDbEnhancedClient().table("Person", PERSON_TABLE_SCHEMA);
        PersonUtils.createPersonTable(personDynamoDbTable, getDynamoDbClient());
        // Use a utility class to add items to the Person table.
        List<Person> personList = PersonUtils.getItemsForCount(2);
        // This utility method performs a put against DynamoDB to save the instances in the list argument.
        PersonUtils.putCollection(getDynamoDbEnhancedClient(), personList, personDynamoDbTable);

        // The first scan logs all items in the table to compare to the results of the subsequent scans.
        final PageIterable<Person> allItems = personDynamoDbTable.scan();
        allItems.items().forEach(p ->
                // 1. Log what is in the table.
                logger.info(p.toString()));

        // Scan for nested attributes.
        PageIterable<Person> streetScanResult = personDynamoDbTable.scan(b -> b
                // Use the 'addNestedAttributeToProject()' or 'addNestedAttributesToProject()' to access data nested in maps in DynamoDB.
                .addNestedAttributeToProject(
                        NestedAttributeName.create("addresses", "work", "street")
                ));

        streetScanResult.items().forEach(p ->
                //2. Log the results of requesting nested attributes.
                logger.info(p.toString()));

        // Scan for a top-level list attribute.
        PageIterable<Person> hobbiesScanResult = personDynamoDbTable.scan(b -> b
                // Use the 'attributesToProject()' method to access first-level attributes.
                .attributesToProject("hobbies"));

        hobbiesScanResult.items().forEach((p) -> {
            // 3. Log the results of the request for the 'hobbies' attribute.
            logger.info(p.toString());
            // To access an item in a list, first get the parent attribute, 'hobbies', then access items in the list.
            String hobby = p.getHobbies().get(1);
            // 4. Log an item in the list.
            logger.info(hobby);
        });
```

```
// Logged results from comment line 1.
Person{id=2, firstName='first name 2', lastName='last name 2', age=11, addresses={work=Address{street='street 21', city='city 21', state='state 21', zipCode='33333'}, home=Address{street='street 2', city='city 2', state='state 2', zipCode='22222'}}, phoneNumbers=[PhoneNumber{type='home', number='222-222-2222'}, PhoneNumber{type='work', number='333-333-3333'}], hobbies=[hobby 2, hobby 21]}
Person{id=1, firstName='first name 1', lastName='last name 1', age=11, addresses={work=Address{street='street 11', city='city 11', state='state 11', zipCode='22222'}, home=Address{street='street 1', city='city 1', state='state 1', zipCode='11111'}}, phoneNumbers=[PhoneNumber{type='home', number='111-111-1111'}, PhoneNumber{type='work', number='222-222-2222'}], hobbies=[hobby 1, hobby 11]}

// Logged results from comment line 2.
Person{id=null, firstName='null', lastName='null', age=null, addresses={work=Address{street='street 21', city='null', state='null', zipCode='null'}}, phoneNumbers=null, hobbies=null}
Person{id=null, firstName='null', lastName='null', age=null, addresses={work=Address{street='street 11', city='null', state='null', zipCode='null'}}, phoneNumbers=null, hobbies=null}

// Logged results from comment lines 3 and 4.
Person{id=null, firstName='null', lastName='null', age=null, addresses=null, phoneNumbers=null, hobbies=[hobby 2, hobby 21]}
hobby 21
Person{id=null, firstName='null', lastName='null', age=null, addresses=null, phoneNumbers=null, hobbies=[hobby 1, hobby 11]}
hobby 11
```

**Note**
If the `attributesToProject()` method follows any other builder method that adds attributes that you want to project, the list of attribute names supplied to the `attributesToProject()` replaces all other attribute names.
A scan performed with the `ScanEnhancedRequest` instance in the following snippet returns only hobby data.

```
ScanEnhancedRequest lastOverwrites = ScanEnhancedRequest.builder()
        .addNestedAttributeToProject(
                NestedAttributeName.create("addresses", "work", "street"))
        .addAttributeToProject("firstName")
        // If the 'attributesToProject()' method follows other builder methods that add attributes for projection,
        // its list of attributes replace all previous attributes.
        .attributesToProject("hobbies")
        .build();
PageIterable<Person> hobbiesOnlyResult = personDynamoDbTable.scan(lastOverwrites);
hobbiesOnlyResult.items().forEach(p ->
        logger.info(p.toString()));

// Logged results.
Person{id=null, firstName='null', lastName='null', age=null, addresses=null, phoneNumbers=null, hobbies=[hobby 2, hobby 21]}
Person{id=null, firstName='null', lastName='null', age=null, addresses=null, phoneNumbers=null, hobbies=[hobby 1, hobby 11]}
```
The following code snippet uses the `attributesToProject()` method first. This ordering preserves all other requested attributes.

```
ScanEnhancedRequest attributesPreserved = ScanEnhancedRequest.builder()
        // Use 'attributesToProject()' first so that the method call does not replace all other attributes
        // that you want to project.
        .attributesToProject("firstName")
        .addNestedAttributeToProject(
                NestedAttributeName.create("addresses", "work", "street"))
        .addAttributeToProject("hobbies")
        .build();
PageIterable<Person> allAttributesResult = personDynamoDbTable.scan(attributesPreserved);
allAttributesResult.items().forEach(p ->
        logger.info(p.toString()));

// Logged results.
Person{id=null, firstName='first name 2', lastName='null', age=null, addresses={work=Address{street='street 21', city='null', state='null', zipCode='null'}}, phoneNumbers=null, hobbies=[hobby 2, hobby 21]}
Person{id=null, firstName='first name 1', lastName='null', age=null, addresses={work=Address{street='street 11', city='null', state='null', zipCode='null'}}, phoneNumbers=null, hobbies=[hobby 1, hobby 11]}
```

## Use complex types in expressions
<a name="ddb-en-client-adv-features-nested-expressions"></a>

You can use complex types in expressions, such as filter expressions and condition expressions, by using dereferencing operators to navigate the structure of the complex type. For objects and maps, use the `. (dot)` and for list elements use `[n]` (square brackets around the sequence number of the element). You can't refer to individual elements of a set, but you can use the [`contains` function](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.OperatorsAndFunctions.html#Expressions.OperatorsAndFunctions.Functions).

The following example show two filter expressions that are used in scan operations. The filter expressions specify the match conditions for items you want in the results. The example uses `Person`, `Address`, and `PhoneNumber` classes shown previously.

```
    public void scanUsingFilterOfNestedAttr() {
        // The following is a filter expression for an attribute that is a map of Address objects.
        // By using this filter expression, the SDK returns Person objects that have an address
        // with 'mailing' as a key and 'MS2' for a state value.
        Expression addressFilter = Expression.builder()
                .expression("addresses.#type.#field = :value")
                .putExpressionName("#type", "mailing")
                .putExpressionName("#field", "state")
                .putExpressionValue(":value", AttributeValue.builder().s("MS2").build())
                .build();

        PageIterable<Person> addressFilterResults = personDynamoDbTable.scan(rb -> rb.
                filterExpression(addressFilter));
        addressFilterResults.items().stream().forEach(p -> logger.info("Person: {}", p));

        assert addressFilterResults.items().stream().count() == 1;

        // The following is a filter expression for an attribute that is a list of phone numbers.
        // By using this filter expression, the SDK returns Person objects whose second phone number
        // in the list has a type equal to 'cell'.
        Expression phoneFilter = Expression.builder()
                .expression("phoneNumbers[1].#type = :type")
                .putExpressionName("#type", "type")
                .putExpressionValue(":type", AttributeValue.builder().s("cell").build())
                .build();

        PageIterable<Person> phoneFilterResults = personDynamoDbTable.scan(rb -> rb
                .filterExpression(phoneFilter)
                .attributesToProject("id", "firstName", "lastName", "phoneNumbers")
        );

        phoneFilterResults.items().stream().forEach(p -> logger.info("Person: {}", p));

        assert phoneFilterResults.items().stream().count() == 1;
        assert phoneFilterResults.items().stream().findFirst().get().getPhoneNumbers().get(1).getType().equals("cell");
    }
```

### Helper method that populates the table
<a name="nested-expressions-helper-method"></a>

```
    public static void populateDatabase() {
        Person person1 = new Person();
        person1.setId(1);
        person1.setFirstName("FirstName1");
        person1.setLastName("LastName1");

        Address billingAddr1 = new Address();
        billingAddr1.setState("BS1");
        billingAddr1.setCity("BillingTown1");

        Address mailing1 = new Address();
        mailing1.setState("MS1");
        mailing1.setCity("MailingTown1");

        person1.setAddresses(Map.of("billing", billingAddr1, "mailing", mailing1));

        PhoneNumber pn1_1 = new PhoneNumber();
        pn1_1.setType("work");
        pn1_1.setNumber("111-111-1111");

        PhoneNumber pn1_2 = new PhoneNumber();
        pn1_2.setType("home");
        pn1_2.setNumber("222-222-2222");

        List<PhoneNumber> phoneNumbers1 = List.of(pn1_1, pn1_2);
        person1.setPhoneNumbers(phoneNumbers1);

        personDynamoDbTable.putItem(person1);

        Person person2 = person1;
        person2.setId(2);
        person2.setFirstName("FirstName2");
        person2.setLastName("LastName2");

        Address billingAddress2 = billingAddr1;
        billingAddress2.setCity("BillingTown2");
        billingAddress2.setState("BS2");

        Address mailing2 = mailing1;
        mailing2.setCity("MailingTown2");
        mailing2.setState("MS2");

        person2.setAddresses(Map.of("billing", billingAddress2, "mailing", mailing2));

        PhoneNumber pn2_1 = new PhoneNumber();
        pn2_1.setType("work");
        pn2_1.setNumber("333-333-3333");

        PhoneNumber pn2_2 = new PhoneNumber();
        pn2_2.setType("cell");
        pn2_2.setNumber("444-444-4444");

        List<PhoneNumber> phoneNumbers2 = List.of(pn2_1, pn2_2);
        person2.setPhoneNumbers(phoneNumbers2);

        personDynamoDbTable.putItem(person2);
    }
```

### JSON representation of items in the database
<a name="nested-attributes-expression-json-items"></a>

```
{
 "id": 1,
 "addresses": {
  "billing": {
   "city": "BillingTown1",
   "state": "BS1",
   "street": null,
   "zipCode": null
  },
  "mailing": {
   "city": "MailingTown1",
   "state": "MS1",
   "street": null,
   "zipCode": null
  }
 },
 "firstName": "FirstName1",
 "lastName": "LastName1",
 "phoneNumbers": [
  {
   "number": "111-111-1111",
   "type": "work"
  },
  {
   "number": "222-222-2222",
   "type": "home"
  }
 ]
}

{
 "id": 2,
 "addresses": {
  "billing": {
   "city": "BillingTown2",
   "state": "BS2",
   "street": null,
   "zipCode": null
  },
  "mailing": {
   "city": "MailingTown2",
   "state": "MS2",
   "street": null,
   "zipCode": null
  }
 },
 "firstName": "FirstName2",
 "lastName": "LastName2",
 "phoneNumbers": [
  {
   "number": "333-333-3333",
   "type": "work"
  },
  {
   "number": "444-444-4444",
   "type": "cell"
  }
 ]
}
```

## Update items that contain complex types
<a name="ddb-en-client-adv-features-nested-updates"></a>

To update an item that contains complex types, you have two basic approaches:
+ Approach 1: First retrieve the item (by using `getItem`), update the object, then call `DynamoDbTable#updateItem`.
+ Approach 2: Don't retrieve the item, but construct a new instance, set the properties you want to update, and submit the instance to `DynamoDbTable#updateItem` by setting the appropriate value of [https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/enhanced/dynamodb/model/IgnoreNullsMode.html](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/enhanced/dynamodb/model/IgnoreNullsMode.html) . This approach does not require that you fetch the item before updating it.

The examples shown in this section use the `Person`, `Address`, and `PhoneNumber` classes shown previously.

### Update approach 1: retrieve, then update
<a name="ddb-en-client-adv-features-nested-updates-retreive"></a>

By using this approach, you ensure that no data is lost on update. The DynamoDB Enhanced Client API recreates the bean with the attributes from the item saved in DynamoDB including values of complex types. You then need to use the getters and setters to update the bean. The downside of this approach is the cost you incur retrieving the item first.

The following example demonstrates that no data is lost if you first retrieve the item before updating it.

```
    public void retrieveThenUpdateExample()  {
        // Assume that we ran this code yesterday.
        Person person = new Person();
        person.setId(1);
        person.setFirstName("FirstName");
        person.setLastName("LastName");

        Address mainAddress = new Address();
        mainAddress.setStreet("123 MyStreet");
        mainAddress.setCity("MyCity");
        mainAddress.setState("MyState");
        mainAddress.setZipCode("MyZipCode");
        person.setMainAddress(mainAddress);

        PhoneNumber homePhone = new PhoneNumber();
        homePhone.setNumber("1111111");
        homePhone.setType("HOME");
        person.setPhoneNumbers(List.of(homePhone));

        personDynamoDbTable.putItem(person);

        // Assume that we are running this code now.
        // First, retrieve the item
        Person retrievedPerson = personDynamoDbTable.getItem(Key.builder().partitionValue(1).build());

        // Make any updates.
        retrievedPerson.getMainAddress().setCity("YourCity");

        // Save the updated bean. 'updateItem' returns the bean as it appears after the update.
        Person updatedPerson = personDynamoDbTable.updateItem(retrievedPerson);

        // Verify for this example.
        Address updatedMainAddress = updatedPerson.getMainAddress();
        assert updatedMainAddress.getCity().equals("YourCity");
        assert updatedMainAddress.getState().equals("MyState"); // Unchanged.
        // The list of phone numbers remains; it was not set to null;
        assert updatedPerson.getPhoneNumbers().size() == 1;
    }
```

### Update approach 2: Use an `IgnoreNullsMode` enum without retrieving the item first
<a name="ddb-en-client-adv-features-nested-updates-nullmode"></a>

To update an item in DynamoDB, you can provide a new object that has only the properties that you want updated and leave the other values as null. With this approach, you need to be aware of how null values in the object are treated by the SDK and how you can control the behavior.

To specify which null-valued properties you want the SDK to ignore, provide an `IgnoreNullsMode` enum when you build the [https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/enhanced/dynamodb/model/UpdateItemEnhancedRequest.Builder.html](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/enhanced/dynamodb/model/UpdateItemEnhancedRequest.Builder.html). As an example of using one of the enumerated values, the following snippet uses the `IgnoreNullsMode.SCALAR_ONLY` mode.

```
// Create a new Person object to update the existing item in DynamoDB.
Person personForUpdate = new Person();
personForUpdate.setId(1);
personForUpdate.setFirstName("updatedFirstName");  // 'firstName' is a top scalar property.

Address addressForUpdate = new Address();
addressForUpdate.setCity("updatedCity");
personForUpdate.setMainAddress(addressForUpdate);

personDynamoDbTable.updateItem(r -> r
                .item(personForUpdate)
                .ignoreNullsMode({{IgnoreNullsMode.SCALAR_ONLY}}));

/* With IgnoreNullsMode.SCALAR_ONLY provided, The SDK ignores all null properties. The SDK adds or replaces
the 'firstName' property with the provided value, "updatedFirstName". The SDK updates the 'city' value of
'mainAddress', as long as the 'mainAddress' attribute already exists in DynamoDB.

In the background, the SDK generates an update expression that it sends in the request to DynamoDB.
The following JSON object is a simplified version of what it sends. Notice that the SDK includes the paths
to 'mainAddress.city' and 'firstName' in the SET clause of the update expression. No null values in
'personForUpdate' are included.

{
  "TableName": "PersonTable",
  "Key": {
    "id": {
      "N": "1"
    }
  },
  "ReturnValues": "ALL_NEW",
  "UpdateExpression": "SET #mainAddress.#city = :mainAddress_city, #firstName = :firstName",
  "ExpressionAttributeNames": {
    "#city": "city",
    "#firstName": "firstName",
    "#mainAddress": "mainAddress"
  },
  "ExpressionAttributeValues": {
    ":firstName": {
      "S": "updatedFirstName"
    },
    ":mainAddress_city": {
      "S": "updatedCity"
    }
  }
}

Had we chosen 'IgnoreNullsMode.DEFAULT' instead of 'IgnoreNullsMode.SCALAR_ONLY', the SDK would have included
null values in the "ExpressionAttributeValues" section of the request as shown in the following snippet.

  "ExpressionAttributeValues": {
    ":mainAddress": {
      "M": {
        "zipCode": {
          "NULL": true
        },
        "city": {
          "S": "updatedCity"
        },
        "street": {
          "NULL": true
        },
        "state": {
          "NULL": true
        }
      }
    },
    ":firstName": {
      "S": "updatedFirstName"
    }
  }
*/
```

The Amazon DynamoDB Developer Guide contains more information about [update expressions](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Expressions.UpdateExpressions.html).

#### Descriptions of the `IgnoreNullsMode` options
<a name="ignore-nulls-mode-descriptions"></a>
+ `IgnoreNullsMode.SCALAR_ONLY` - Use this setting to update scalar attributes at any level. The SDK constructs an update statement that sends only non-null, scalar attributes to DynamoDB. The SDK ignores null-valued, scalar attributes of a bean or map, retaining the saved value in DynamoDB.

  When you update a scalar attribute of map or bean, the map must already exists in DynamoDB. If you add a map or a bean to the object that does not already exist for the object in DynamoDB, you get a `DynamoDbException` with the message *The document path provided in the update expression is invalid for update*. You must use `MAPS_ONLY` mode to add a bean or map to DynamoDB before you update any of its attributes.
+ `IgnoreNullsMode.MAPS_ONLY` - Use this setting to add or replace properties that are a bean or a map. The SDK replaces or adds any map or bean provided in the object. Any beans or maps that are null in the object are ignored, retaining the map that exists in DynamoDB.
+ `IgnoreNullsMode.DEFAULT` - With this setting, the SDK never ignores null values. Scalar attributes at any level that are null are updated to null. The SDK updates any null-valued bean, map, list, or set property in the object to null in DynamoDB. When you use this mode—or don't provide a mode since it's the default mode—you should retrieve the item first so that values in DynamoDB are not set to null that are provided in the object for updating, unless your intention is to set the values to null.

In all modes, if you provide an object to `updateItem` that has a non-null list or set, the list or set is saved to DynamoDB.

#### Why the modes?
<a name="ddb-en-client-adv-features-nested-updates-nullmodes-why"></a>

When you provide an object with a bean or map to the `updateItem` method, the SDK can't tell if it should use the property values in the bean (or entry values in the map) to update the item, or if the entire bean/map should replace what's been saved to DynamoDB.

Working from our previous example that shows the retrieval of the item first, let's attempt to update the `city` attribute of `mainAddress` without the retrieval.

```
/* The retrieval example saved the Person object with a 'mainAddress' property whose 'city' property value is "MyCity".
/* Note that we create a new Person with only the necessary information to update the city value
of the mainAddress. */
Person personForUpdate = new Person();
personForUpdate.setId(1);
// The update we want to make changes the city.
Address mainAddressForUpdate = new Address();
mainAddressForUpdate.setCity("YourCity");
personForUpdate.setMainAddress(mainAddressForUpdate);

// Lets' try the following:
Person updatedPerson = personDynamoDbTable.updateItem(personForUpdate);
/*
 Since we haven't retrieved the item, we don't know if the 'mainAddress' property
 already exists, so what update expression should the SDK generate?

A) Should it replace or add the 'mainAddress' with the provided object (setting all attributes to null other than city)
   as shown in the following simplified JSON?

      {
        "TableName": "PersonTable",
        "Key": {
          "id": {
            "N": "1"
          }
        },
        "ReturnValues": "ALL_NEW",
        "UpdateExpression": "SET #mainAddress = :mainAddress",
        "ExpressionAttributeNames": {
          "#mainAddress": "mainAddress"
        },
        "ExpressionAttributeValues": {
          ":mainAddress": {
            "M": {
              "zipCode": {
                "NULL": true
              },
              "city": {
                "S": "YourCity"
              },
              "street": {
                "NULL": true
              },
              "state": {
                "NULL": true
              }
            }
          }
        }
      }

B) Or should it update only the 'city' attribute of an existing 'mainAddress' as shown in the following simplified JSON?

      {
        "TableName": "PersonTable",
        "Key": {
          "id": {
            "N": "1"
          }
        },
        "ReturnValues": "ALL_NEW",
        "UpdateExpression": "SET #mainAddress.#city = :mainAddress_city",
        "ExpressionAttributeNames": {
          "#city": "city",
          "#mainAddress": "mainAddress"
        },
        "ExpressionAttributeValues": {
          ":mainAddress_city": {
            "S": "YourCity"
          }
        }
      }

However, assume that we don't know if the 'mainAddress' already exists. If it doesn't exist, the SDK would try to update
an attribute of a non-existent map, which results in an exception.

In this particular case, we would likely select option B (SCALAR_ONLY) to retain the other values of the 'mainAddress'.
*/
```

The following two examples show uses of the `MAPS_ONLY` and `SCALAR_ONLY` enumerated values. `MAPS_ONLY` adds a map and `SCALAR_ONLY` updates a map.

##### `IgnoreNullsMode.MAPS_ONLY` example
<a name="scalar-only-example"></a>

```
    public void mapsOnlyModeExample() {
        // Assume that we ran this code yesterday.
        Person person = new Person();
        person.setId(1);
        person.setFirstName("FirstName");

        personDynamoDbTable.putItem(person);

        // Assume that we are running this code now.

        /* Note that we create a new Person with only the necessary information to update the city value
        of the mainAddress. */
        Person personForUpdate = new Person();
        personForUpdate.setId(1);
        // The update we want to make changes the city.
        Address mainAddressForUpdate = new Address();
        mainAddressForUpdate.setCity("YourCity");
        personForUpdate.setMainAddress(mainAddressForUpdate);

        Person updatedPerson = personDynamoDbTable.updateItem(r -> r
                .item(personForUpdate)
                .ignoreNullsMode(IgnoreNullsMode.MAPS_ONLY)); // Since the mainAddress property does not exist, use MAPS_ONLY mode.
        assert updatedPerson.getMainAddress().getCity().equals("YourCity");
        assert updatedPerson.getMainAddress().getState() == null;
    }
```

##### `IgnoreNullsMode.SCALAR_ONLY example`
<a name="maps-only-example"></a>

```
    public void scalarOnlyExample() {
        // Assume that we ran this code yesterday.
        Person person = new Person();
        person.setId(1);
        Address mainAddress = new Address();
        mainAddress.setCity("MyCity");
        mainAddress.setState("MyState");
        person.setMainAddress(mainAddress);

        personDynamoDbTable.putItem(person);

        // Assume that we are running this code now.

        /* Note that we create a new Person with only the necessary information to update the city value
        of the mainAddress. */
        Person personForUpdate = new Person();
        personForUpdate.setId(1);
        // The update we want to make changes the city.
        Address mainAddressForUpdate = new Address();
        mainAddressForUpdate.setCity("YourCity");
        personForUpdate.setMainAddress(mainAddressForUpdate);

        Person updatedPerson = personDynamoDbTable.updateItem(r -> r
                .item(personForUpdate)
                .ignoreNullsMode(IgnoreNullsMode.SCALAR_ONLY)); // SCALAR_ONLY mode ignores null properties in the in mainAddress.
        assert updatedPerson.getMainAddress().getCity().equals("YourCity");
        assert updatedPerson.getMainAddress().getState().equals("MyState"); // The state property remains the same.
    }
```

Refer to the following table to see which null values are ignored for each mode. You can often work with either `SCALAR_ONLY` and `MAPS_ONLY` except when you work with beans or maps.

**Which null-valued properties in the object submitted to `updateItem` does the SDK ignore for each mode?**

| Type of property | in SCALAR\_ONLY mode | in MAPS\_ONLY mode | in DEFAULT mode |
| --- | --- | --- | --- |
| Top scalar | Yes | Yes | No |
| Bean or map | Yes | Yes | No |
| Scalar value of a bean or map entry | Yes1 | No2 | No |
| List or set | Yes | Yes | No |

1This assumes the map already exists in DynamoDB. Any scalar value—null or not null—of the bean or map that you provide in the object for update requires that a path to the value exists in DynamoDB. The SDK constructs a path to the attribute by using the `. (dot)` dereference operator before it submits the request.

2Since you use `MAPS_ONLY` mode to fully replace or to add a bean or map, all null values in the bean or map are retained in the map saved to DynamoDB.
