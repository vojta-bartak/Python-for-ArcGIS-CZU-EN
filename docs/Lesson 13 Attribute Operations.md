# Lesson 13: Attribute Operations

In this lesson, we will discuss the operations you are usually used to performing "manually" in the ArcGIS graphical user environment, often by right-clicking on an attribute table field or layer and selecting a tool from their context menu. These operations include, for example:

- Add a new field to an attribute table.
- Delete an existing attribute table field.
- Calculate field values using the *Field calculator* or *Calculate geometry* tools.
- Summarize values of some field/fields of an attribute table.
- Link tables using *Join* or *Relate*.
- Attribute selection of features (table rows) using SQL query.

In fact, for all these "manual" operations, there are corresponding geoprocessing tools in the ArcToolbox that allow them to be performed within models from Model Builder or within scripts in Python. Most of them are located in the *Data Management Tools* toolbox.

## Motivation task

We will demonstrate the above-mentioned tasks by solving the following complex task:

> Calculate the volume of surface runoff for individual cadastres in the Liberec region. Surface runoff (in liters per second) is calculated according to the formula $Q = S*\Psi*q$, where $S$ is the size of the drained area in square meters, $\Psi$ is the dimensionless runoff coefficient according to Nyplt and Viessmann (reflects the type of surface, surface treatment and its roughness) and $q$ is the annual total precipitation in millimeters.

First, download and view the required [data](https://owncloud.cesnet.cz/index.php/s/R9f1NAoQBbXtMrd). Data description ...

Outline of the solution ...

## Add and delete fields

Tools for working with attribute table fields, such as adding fields, deleting fields, or calculating field values, can be found in the *Data Management Tools -> Fields* toolset.

Adding a field is done with the **Add Field** tool. We will demonstrate its use on the example of adding the text field "NEWFIELD" to the table of the layer "obce_LK". We can perform the operation, for example, in the *Python window* in the ArcMap map document, so that we can immediately view the result.

```console
>>> arcpy.management.AddField("obce_LK", "NEWFIELD", "TEXT")
```

> **Task 1.** Enter the above command in the *Python window* command line and view the result in the attribute table.

As can be seen from the example, the first parameter of the tool is the name of the input table (if a feature class is specified, then its attribute table is used). The second parameter is the name of the field to be added. The third parameter is the field data type (for a complete list of types that can be used, see the tool's help). With the other optional parameters, we could set restrictions for the given format, such as the maximum length of a text string (in the case of a text field), the number of valid digits (*scale*) and decimal places (*precision*) in the case of a numeric type, etc. In the example above, we are satisfied with the default settings of these parameters.)

When adding a field, make sure that the field with the given name is not already present in the table. If so, the *Add Field* tool adds the field anyway and only alerts you to the existence of the original field with a "Warning" message. This will, obviously, permanently delete the original field.

Existing fields (if not required, such as FID or Shape fields) can be deleted using the ** Delete Field ** tool (* Data Management Tools -> Fields *). Its use is obvious (if not, read the help for this tool).

> ** Task 2. ** Delete the fields you created in task 1 again with the * Delete Field * tool.

## Joining tables

Joining tables using the *join* method results in adding a field (or fields) from the joined table to the target table, based on some common attribute (so-called *keys*). This type of connection is possible in case one row of the target table corresponds to at most one row of the joined table (otherwise it would not be possible to decide which row of the joined table should be connected to the given row of the target table). At the same time, multiple rows of the target table can correspond to one row of the joined table. This is because a row of the joined table can be copied to any number of rows in the target table.

In addition to the *join* method, the *relate* method is also available in ArcGIS, which allows you to define a relation when one row of the target table corresponds to multiple rows of the joined table. However, this method cannot be used with Python, resp. ArcPy package. Therefore, we will focus only on the *join* method.

There are two ways to connect table by the *join* method:

- as a temporary link, which is defined only within layers,
- as a permanent extension of the target table by new columns, copied from the attached table.

### Temporary join

Temporary join is just the way you're probably used to doing it "manually" in ArcGIS.

Because the temporary link is defined at the layer level, not the dataset, you must first create a layer from the source dataset to be able to join it temporarily with another table. We are used to work with layers in ArcMap as a standard thing. However, layers can be created in Python as well. Such layer will be created in the operating memory and will be stored in a variable with which it will be possible to work with it, even if cannot view it in a map document. At the same time, it will have a name chosen by the user, under which it can be further referenced in the code.

The layer is created with the **Make Feature Layer** tool from the *Data Management Tools* toolbox. Its first parameter is the path to the dataset from which we want to create the layer, the second parameter is the name of the layer. The result of the tool call (object of class *Result*) can be stored in a variable, which will then represent the layer in other tools.

```Python
lyr = arcpy.management.MakeFeatureLayer(r"C:\...\UrbanAtlas_LK.shp", "lyr")
```

If we have created a layer, we can define its connection with some other table using the tool **Add Join** from *Data Management Tools -> Joins*. In the following example, a table of runoff coefficient values for individual surface types is attached to the attribute table of land cover polygons from the Urban Atlas database (see the motivational task at the beginning of the lesson). The common column (key) used to specify the connection is the "CODE" attribute, which is the code of the land cover class. Once connected, a list of column names of the created layer to which the table has been attached is listed:

```Python
import arcpy

# inputs
land_cover = "UrbanAtlas_LK.shp"
coef_infil = "coef.dbf"

# create a layer from the dataset
lyr = arcpy.management.MakeFeatureLayer (land_cover, "lyr")

# join
arcpy.management.AddJoin (lyr, "CODE", coef_infil, "CODE")

# print fields of the newly created layer
for field in arcpy.ListFields (lyr):
    print (field.name)
```

The result is as follows:

```console
UrbanAtlas_LK.FID
UrbanAtlas_LK.Shape
UrbanAtlas_LK.CITIES
UrbanAtlas_LK.LUZ_OR_CIT
UrbanAtlas_LK.CODE
UrbanAtlas_LK.ITEM
UrbanAtlas_LK.PROD_DATE
UrbanAtlas_LK.SHAPE_LEN
UrbanAtlas_LK.SHAPE_AREA
UrbanAtlas_LK.srazky
coef.OID
coef.kod
coef.name
coef.cesky
coef.ko_vsak
coef.CODE
```

As you can see, in the layer table, the column names are supplemented by the name of the table from which the columns came. As a result, we can refer to columns from the joined table in this layer.

> **Task 3.** Run the script with the above code. *Warning*: The script assumes that the ArcGIS working directory is set to the folder in which we have the data. If this is not the case for you, you need to add the appropriate command to the script.

As already mentioned, the connection with *Add Join* is only temporary because it takes place in the layer, not in the source dataset. If you no longer need to link the tables, you must remove the connection from the layer using the **Remove Join** tool (*Data Management Tools -> Joins*). Below is its use and subsequent listing of the attributes of the layer from which the link was removed:

```console
>>> arcpy.management.RemoveJoin(lyr)
<Result 'lyr'>
>>> for f in arcpy.ListFields(lyr): print(f.name)

FID
Shape
CITIES
LUZ_OR_CIT
CODE
ITEM
PROD_DATE
SHAPE_LEN
SHAPE_AREA
precipitation
```

It can be seen that the return value of the tool is again an object of class *Result*, representing the layer. However, we already have this layer stored in the `lyr` variable.

Instead of deleting the link, you can also delete the layer. However, it is not enough to use the Python command `del`, it is necessary to delete the layer with the **Delete** tool from the ArcPy package:

```console
>>> arcpy.management.Delete(lyr)
<Result 'true'>
```

Deleting a layer is important because whenever a layer is created from a dataset, that dataset is "locked", ie a lock file is created to prevent any program from making changes to the dataset. For example, if we want to add or delete fields in a dataset, it will not be possible if a layer is created from it. After deleting a layer, the lock file is also deleted and the dataset is unlocked for editing.

### Permanent join

If we want to join a field permanently, we have two options:

- We first perform a temporary join as described above, and then save the resulting layer to a new dataset, eg with the **Copy Features** tool (*Data Management Tools -> General*).
- We join the field directly to the source dataset table using the **Join Field** tool (*Data Management Tools -> Joins*). With this option, it is possible to join either all fields or only selected ones. Joined fields become a permanent part of the target table.

> **Task 4.** Use the *Join Field* tool to attach a field with coefficient values ("ko_vsak") from the runoff coefficient table as a permanent new field to the land cover table. (Refer to the tool's syntax for help.) View the resulting table. Then delete the new field back with the *Delete Field* tool.

## Calculate field values

Field values can be calculated using the **Calculate Field** tool from the *Fields* toolset of the *Data Management Tools* toolbox. The first parameter is the path to the input dataset, the second is the name of the field we want to calculate. The calculation expression follows.

The following example presents the simplest possible calculation, where the whole field is filled with a constant value. First, we add an integer field named "CONST" to the dataset "obce_LK.shp" and fill it with the constant value 100. Then we add a text field named "MESSAGE" in a similar way and fill it with the text "Hello world!":

```python
import arcpy

obce = "obce_LK.shp"

# Add a numeric (integer) field
arcpy.management.AddField(obce, "CONST", "LONG")

# Fill the field with a constant of 100
arcpy.management.CalculateField(obce, "CONST", 100)

# Add a text field
arcpy.management.AddField(obce, "MESSAGE", "TEXT")

# Fill the field with a constant of 100
arcpy.management.CalculateField(obce, "MESSAGE", '"Hello world!"')
```

Note that the expression "Hello world!" had t be written using both types of quotes: `'"Hello world!"'`. This is because in the case of text, the expression must include quotation marks, and the expression itself is also passed to the tool as text. The outer, single quotes enclose the entire text of the expression, while the inner, double quotes are already part of the expression itself and indicate that the content of the expression is text. (These outer quotation marks correspond to the quotation marks that we would be forced to use in the *Field Calculator* window when "manually" solving this field calculation.)

> **Task 5.** Using the above script, add the given fields to the cadasters dataset and fill them with some constant value. View the result in ArcGIS. Then delete the fields again (using Python).

When calculating a field, it is possible to use values of any other field that already exists. This field can be referenced by its name embraced by exclamation marks (see below). We can freely combine values of various fields, perform calculations with them, etc. We can also use any function or operation in the expression that is part of the basic equipment of Python. All you have to do is specify the fourth, optional parameter of the *Calculate Field* tool, saying which language is used in the expression. The choice of language also affects how we refer to other fields (the exclamation marks are used only in the case of Python language). In the example below, we use the "PYTHON_9.3" language specification, which is a Python-based expression language, as it has been used since ArcGIS 9.3.

In the code below, we first add a new field "NAZEV_2" to the dataset "obce_LK.shp". Then we fill this field with English names of the cadasters, which are stored in the field "NAZEV_ENG", but converted to capital letters. In Python, you can to convert any text string to uppercase resp. lowercase letters using the string method `upper` resp. `lower`:

```console
>>> "HelLo".upper()
'HELLO'
>>> "HelLo".lower()
'hello'
```

Now the code itself:

```python
import arcpy

obce = "obce_LK.shp"

# add a new field
arcpy.management.AddField(obce, "NAZEV_2", "TEXT")

# fill the field with uppercase names from the field NAZEV_ENG
arcpy.management.CalculateField(obce, "NAZEV_2", '!NAZEV_ENG!.upper()', "PYTHON_9.3")
```

Note the use of exclamation marks to reference the "NAZEV_ENG" field within the expression, and the use of the `upper` method.

> **Task 6.** In the same way as in the previous example, create a field with the names of municipalities written in lowercase letters.

A very common task is to calculate geometric properties of features into an attribute. An example is the calculation of polygon areas in an attribute called eg "AREA_KM". The "manual" solution would be to use the *Calculate Geometry* tool available in the context menu of the field. In Python, the operation is performed again using the *Calculate Field* tool, where within the expression we refer to the special field "Shape" and its property "area" using `!Shape.area!` (If we want the result in square kilometers, it is necessary to include units conversion in the expression):

```python
import arcpy

obce = "obce_LK.shp"

# add a new field for areas
arcpy.management.AddField(obce, "AREA_KM", "DOUBLE")

# fill the field with areas in squared kilometers
arcpy.management.CalculateField(obce, "AREA_KM", '!shape.area!/1000000', "PYTHON_9.3")
```

> **Task 7.** Add the "PARATIO" field to the "UrbanAtlas_LK.shp" dataset and calculate the "Perimeter-Area Ratio", which is a landscape metric describing the degree of shape complexity of landscape patches.

## Summarizing fields

Completion of the motivation task ...

## Attribute selections

An SQL query and when it occurs...

Select...

Repeated selection in a layer .. (eg filling in a field according to an attribute?)

Save layer?

## Summary

## Tasks