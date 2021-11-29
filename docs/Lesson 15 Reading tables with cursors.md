# Lesson 15: Reading tables with cursors

In this lesson, you will learn how to browse attribute tables (or other tables in `.dbf` format) line by line and read and write values from/to individual fields (columns). We will test individual procedures on [data](https://owncloud.cesnet.cz/index.php/s/87mECJH9RhNIdVz) of regions (polygons) and large cities (points) of the Czech Republic.

> **Task 1.** Start a new ArcGIS project and view the data, including attribute tables.

The table is browsed using the so-called *cursor*, which is an object similar to what we create when opening text files with the `open` function: it mediates the connection with the given file (table), so it is locked for editing by any other applications as long as we browse it. For this reason, it is necessary to delete the created cursor after finishing work with the table (with the command `del`), similarly to closing a text file (where we use the `close` method.

Cursors in `arcpy` are of three types:

- **Search Cursor** - only for reading values from the table,
- **Update Cursor** - for reading and writing to existing table rows,
- **Insert Cursor** - for inserting new rows into the table and deleting existing rows.

## Read rows using the *Search* cursor

The syntax for using a cursor is as follows:

```python
tab = arcpy.da.SearchCursor(in_table, field_names, {where_clause}, ...)
```

In the given code we store the cursor in the variable `tab`. The `arcpy.da.` section refers to the fact that the cursors in the `arcpy` package are implemented in a separate `da` module (short for "Data Access"). The cursor object (ie object of the class *SearchCursor*) is created by the class constructor of the same name (`SearchCursor` function in the example). The most important parameters of the function are:

- **in_table** - table to be opened (the whole path as a string, or a relative path with respect to the working directory) - it can be a shapefile, feature class, feature layer, `.dbf` table, or a table view.
- **field_names** - list of fields (columns) we want to open (Python list of strings),
- **where_clause** - SQL query (optional) with which we can limit the opened table only to selected rows.

The cursor contains other parameters (shown in the example by three dots), but we will leave them aside here.

The cursor can be browsed directly by a `for` cycle. The iteration variable goes through the individual lines and always takes a value of a tuple of length *n*, ie the same length as the the number of open fields. Let's look at an example of opening the "CATEGORY" and "NAME" attributes of the dataset of cities:

```python
import arcpy
arcpy.env.workspace = r"C:\my_path\..."
tab = arcpy.da.SearchCursor("Sidla_body.shp", ["NAZEV", "KATEGORIE"])
for r in tab:
    print(r)
del(tab)
```

After running the script we get the following output:

```console
(u'Praha', 1)
(u'Brno', 2)
(u'Plze\u0148', 2)
(u'Ostrava', 2)
(u'Karlovy Vary', 3)
(u'Zl\xedn', 3)
(u'Chomutov', 3)
(u'Most', 3)
(u'\xdast\xed nad Labem', 3)
(u'Kladno', 3)
(u'Hradec Kr\xe1lov\xe9', 3)
(u'Karvin\xe1', 3)
(u'Pardubice', 3)
(u'Fr\xfddek-M\xedstek', 3)
(u'Hav\xed\u0159ov', 3)
(u'Liberec', 3)
(u'\u010cesk\xe9 Bud\u011bjovice', 3)
(u'Olomouc', 3)
```

Because each row is represented by a tuple, we can access the individual items (ie columns) of it using indexes:

```python
# -*- coding: cp1250 -*-

import arcpy
arcpy.env.workspace = r"C:\my_path\..."
tab = arcpy.da.SearchCursor("Sidla_body.shp", ["NAZEV", "KATEGORIE"])
for r in tab:
    print(u"City of the category " + str(r[1]) + " is called " + r[0] + ".")
del(tab)
```

The output is:

```console
City of the category 1 is called Praha.
City of the category 2 is called Brno.
City of the category 2 is called Plzeň.
City of the category 2 is called Ostrava.
City of the category 3 is called Karlovy Vary.
City of the category 3 is called Zlín.
City of the category 3 is called Chomutov.
City of the category 3 is called Most.
City of the category 3 is called Ústí nad Labem.
City of the category 3 is called Kladno.
City of the category 3 is called Hradec Králové.
City of the category 3 is called Karviná.
City of the category 3 is called Pardubice.
City of the category 3 is called Frýdek-Místek.
City of the category 3 is called Havířov.
City of the category 3 is called Liberec.
City of the category 3 is called České Budějovice.
City of the category 3 is called Olomouc.
```

Notice that when opening the table, we have changed the order of the columns compared to how the table appears in ArcGIS. When opening a table with the cursor, we can select any columns in any order, we can even open one column in several copies (which rarely has a good reason). When reading values from a row, the order of the items is exactly the order in which we sorted the columns when creating the cursor.

In the previous example, we did not use the optional parameter *where_clause*, which we can use to restrict which rows are to be read. For example, if we only wanted to open records for first and second category cities, the code would look like this:

```python
import arcpy
arcpy.env.workspace = r"C:\my_path\..."
tab = arcpy.da.SearchCursor("Sidla_body.shp", ["NAZEV"], '"KATEGORIE" < 3')
for r in tab:
    print(r[0])
del(tab)
```

The result:

```console
Praha
Brno
Plzeň
Ostrava
```

The `for` loop is not the only way to browse a table. If we only want to make a single one row move in the table, we can use the cursor method `next`, which returns the current row and at the same time moves the cursor position to the next row. In this way, for example, it is possible to read the contents of the, say, eighteenth line:

```python
import arcpy
arcpy.env.workspace = r"C:\my_path\CR_kraje_sidla_toky"
tab = arcpy.da.SearchCursor("Sidla_body.shp", ["NAZEV", "KATEGORIE"])
for i in range(18):
    r = tab.next()
print(r)
del(tab)
```

```console
(u'Olomouc', 3)
```

When browsing the table, the cursor can only be moved forward. If we get to the end of the table (either by the `for` loop or the` next` method), the table can no longer be browsed. To do this, you must recreate the cursor.

Finally, let's look at how to avoid the necessity of explicit deletion of the cursor after use, thanks to the `with` clause, which you know (in a similar context) from the lesson on text files:

```python
import arcpy
arcpy.env.workspace = r"C:\my_path\..."
with arcpy.da.SearchCursor("Sidla_body.shp", ["NAZEV"], '"KATEGORIE" < 3') as tab:
    for r in tab:
        print(r[0])
# Here the table is closed and the cursor object deleted
```

> **Task 2**. Open the table of regions and write down their names and population numbers.

> **Task 3.** Use the cursor to find the region with the largest number of women over men.

> **Task 4.** Use the cursor to calculate the shape index (perimeter divided by the area) of each polygon. (Hint: first add the "Area" and "Perimeter" fields to the table and use the *Calculate Field* tool to calculate their values. Then use the cursor to read the table and divide these values.)

## Overwrite values in a row with *Update* cursor

If we want to not only read the contents of the table, but also change them, we use the *Update* cursor. The syntax is practically the same as for the *Search* cursor:

```python
tab = arcpy.da.UpdateCursor("Sidla_body.shp", ["NAZEV", "KATEGORIE"])
```

The difference is what methods the respective cursor has available (in the previous section we used, for example, the `next` method, which is also available in the *Update* cursor). A new method, specific for the *Update* cursor, is the *updateRow* method, which can be used to replace the line on which the cursor is located with another line. This must be passed to the method in the form of a tuple or list of an appropriate length, while the individual items and their data types must correspond to the open columns.

In the following example, we will change the category of the city of Brno from 2 to 3 (this does not indicate anything bad about this city!):

```python
import arcpy
arcpy.env.workspace = r"C:\my_path\CR_kraje_sidla_toky"
tab = arcpy.da.UpdateCursor("Sidla_body.shp", ["NAZEV", "KATEGORIE"], 
                            '"NAZEV" = \'Brno\'')
tab.next()
tab.updateRow(("Brno", 3))
del(tab)
```

Note that we only opened the line with Brno. Nevertheless, we had to use the `next` method to move the cursor to this first line.

> **Task 5.** Add the text field "STATUS" to the table of regions and fill in the value "OK" for those regions where there are deaths than births and "KO" for others.

## Delete a row

Another use of the *Update* cursor is to delete a row. We will now use this and try to erase the city of Brno from the world map for good. However, since we will subsequently want to undo our terrible act and use the *Insert* cursor to return Brno to the world map, it will be appropriate to save the relevant record somewhere in advance, for example as follows:

```python
with arcpy.da.SearchCursor("Sidla_body.shp", ["SHAPE@", "NAZEV", "KATEGORIE"],
                          '"NAZEV" = \'Brno\'') as tab:
    brno = tab.next()
```

It is especially important to keep the contents of the *Shape* column here, which is done using the name `"SHAPE@"` (this field and its use will be thoroughly explained in the next lesson). The geometry of the feature (in our case the coordinates of the city of Brno) is stored in this field, which we will need when restoring it.

Now the execution itself:

```python
with arcpy.da.UpdateCursor("Sidla_body.shp", ["SHAPE@", "NAZEV", "KATEGORIE"],
                          '"NAZEV" = \'Brno\'') as tab:
    tab.next()
    tab.deleteRow()
```

See the result in the table of cities as well as in the map...

## Add a new line with *Insert* cursor

Now, as we have announced, we have realized the impact of our brutal act. Fortunately, there is an *Insert* cursor, allowing us to insert a new row into the table. It has a simpler syntax because it does not allow us to filter open rows using an SQL query. The only thing we can influence is which columns we open. A new row is always added to the end of the table (even in the case of such an important city as Brno).

If we work with an attribute table of the vector layer, it is necessary to keep in mind that whenever we add as a new record, it is necessary to feed the *Shape* field of the table with a corresponding geometry of the added feature. Otherwise, the new line, which should correspond to a feature, will lack a geometry and the whole layer would be damaged and unusable. Fortunately, in the case of Brno, we saved the geometry, so it is not a problem to return it to the table again:

```python
with arcpy.da.InsertCursor("Sidla_body.shp", ["SHAPE@", "NAZEV", "KATEGORIE"]) as tab:
    tab.insertRow(brno)
```

We can only hope that you did the whole procedure of deleting and rescuing Brno in one session, ie that you did not restart the console in the meantime. The variable `brno` would be deleted and the city lost forever...

## Old cursor types

## Summary

## Exercises

1. Write a script that calculates the average shape index for each land cover class for a polygon land cover layer. Solve without cursors.
2. Solve the previous task with the help of cursors, save the result in a table in the format `.csv`.