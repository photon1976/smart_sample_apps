"""
Cron job to update SMArt medication list from a surescripts feed

Josh Mandel
joshua.mandel@childrens.harvard.edu
"""
from ss_utils import put_ccr_to_smart, get_smart_client
from regenstrief import SSClient
import sys, time

def sync_regenstrief():
#    regenstrief_client = SSClient()
    smart_client = get_smart_client()
    print dir(smart_client)

    sparql = """PREFIX  rdf:  <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX  foaf:  <http://xmlns.com/foaf/0.1/>
CONSTRUCT {?person rdf:type foaf:Person} 
WHERE   {
  ?person foaf:givenName "Betty".
  ?person rdf:type foaf:Person.
}
order by ?ln"""


    print  smart_client.get("/records/search", data={'sparql':sparql})
            
    for record_id in smart_client.loop_over_records():
        print "not a SS patient, but here's the med list..."
        continue
        
        print "Deleting old meds ", record_id, time.time()        
        smart_client.records_X_medications_DELETE()        

        print "Getting CCR ", record_id, time.time()        
        d = smart_client.records_X_demographics_GET()
        dispensed_ccr =  regenstrief_client.get_dispensed_meds(d)        
        
        print "Got CCR: ", time.time()
        put = put_ccr_to_smart(smart_client, record_id, dispensed_ccr)

if __name__ == "__main__":
    sync_regenstrief()
