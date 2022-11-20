import dtlpy as dl
import datetime as tm

dl.login()
# Create a Project
project = dl.projects.create(project_name='Try')
# 2a Create a dataset
dataset = project.datasets.create(dataset_name='Assignment')
# 2b upload items
items = dataset.items.upload(
    local_path='C:\\Users\\relz2\\Desktop\\pic', remote_path='/folder')
# 2c add three labels
dataset.add_label(label_name='class1')
dataset.add_label(label_name='class2')
dataset.add_label(label_name='key')

# get item id
ds = dataset.items.get_all_items()
# 2d updated UTM to item
item1 = dataset.items.get(item_id='637930b2bfdf183bdec9bbbb')
item1.metadata['collected'] = [f'tm.datetime.now()']
item1.update()

# 2e
item1 = dataset.items.get(item_id='637930b2bfdf183bdec9bbbb')
builder = item1.annotations.builder()
builder.add(annotation_definition=dl.Classification(label='class1'))
item1.annotations.upload(builder)

item2 = dataset.items.get(item_id='637930aac48b390e17e0bb68')
builder = item2.annotations.builder()
builder.add(annotation_definition=dl.Classification(label='class1'))
item2.annotations.upload(builder)

# 2f
item3 = dataset.items.get(item_id='637930b01fdb06530a5e5ff3')
builder = item3.annotations.builder()
builder.add(annotation_definition=dl.Classification(label='class2'))
item3.annotations.upload(builder)

item4 = dataset.items.get(item_id='6379309ac48b3908a4e0bb65')
builder = item4.annotations.builder()
builder.add(annotation_definition=dl.Classification(label='class2'))
item4.annotations.upload(builder)

item5 = dataset.items.get(item_id='637930b3d4207868c1785f38')
builder = item5.annotations.builder()
builder.add(annotation_definition=dl.Classification(label='class2'))
item5.annotations.upload(builder)

# 2g
builder = item3.annotations.builder()
builder.add(annotation_definition=dl.Point(x=80, y=80, label='key'))
builder.add(annotation_definition=dl.Point(x=120, y=120, label='key'))
builder.add(annotation_definition=dl.Point(x=50, y=110, label='key'))
builder.add(annotation_definition=dl.Point(x=120, y=80, label='key'))
builder.add(annotation_definition=dl.Point(x=80, y=40, label='key'))
item3.annotations.upload(builder)

# 3
my_filter = dl.Filters()
my_filter.add_join(field='labels', values='class1')
pages = dataset.items.list(filters=my_filter)
for item in pages.all():
    print(item.name)
    print(item.id)

# 4
points_filter = dl.Filters(resource=dl.FiltersResource.ANNOTATION)
points_filter.add(field='point', values='key')
key_pages = dataset.annotations.list(filters=points_filter)
for item in key_pages.all():
    print(item.name)
    print(item.id)
    for annotation in item:
        print(annotation.id, annotation.label, annotation.position)
        
