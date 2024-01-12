from pygbif import registry
from pygbif import occurrences
from pygbif import species
import json


# UUID found in dataset documentation: https://registry.gbif.org/dataset/f06fef3c-6ea6-4345-b724-a1b8e490dc55/identifier
UUID = "f06fef3c-6ea6-4345-b724-a1b8e490dc55"
# x = registry.dataset_metrics(uuid='f06fef3c-6ea6-4345-b724-a1b8e490dc55')
# Metrics missing for SEO
# registry.datasets(type=None, uuid=None, query=None, id=None, limit=100, offset=None, **kwargs)
metaDataOfDataset = registry.datasets(data='metadata', uuid=UUID)

dataset = registry.datasets(data="all", uuid=UUID, type="OCCURENCE")
# The groups of birds covered in the dataset
dataset["taxonomicCoverages"]

# Look up suggested names for this species -> some species have more than one accepted scientific name
beeEater = species.name_suggest("Merops apiaster")
print(json.dumps(beeEater, indent=2))
beeEater = species.name_backbone("Merops apiaster")

# Search for occurences of the bee eater in the dataset
# occurrences.search(repatriated=None, kingdomKey=None, phylumKey=None, classKey=None, orderKey=None, familyKey=None, genusKey=None, subgenusKey=None, scientificName=None, country=None, publishingCountry=None, hasCoordinate=None, typeStatus=None, recordNumber=None, lastInterpreted=None, continent=None, geometry=None, recordedBy=None, recordedByID=None, identifiedByID=None, basisOfRecord=None, datasetKey=None, eventDate=None, catalogNumber=None, year=None, month=None, decimalLatitude=None, decimalLongitude=None, elevation=None, depth=None, institutionCode=None, collectionCode=None, hasGeospatialIssue=None, issue=None, q=None, spellCheck=None, mediatype=None, limit=300, offset=0, establishmentMeans=None, facet=None, facetMincount=None, facetMultiselect=None, **kwargs)
beeEaterOccurences = occurrences.search(taxonKey=beeEater["speciesKey"], datasetKey=UUID, hasCoordinate=True)

chiffChaff = species.name_backbone("Phylloscopus collybita")
print(json.dumps(chiffChaff, indent=2))
chiffChaffOccurences = occurrences.search(taxonKey=chiffChaff["speciesKey"], datasetKey=UUID, hasCoordinate=True)
occurrences.count(taxonKey=chiffChaff["speciesKey"])