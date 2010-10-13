
from smpp.esme import *


print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"

#esme = ESME()
#esme.connect_SMSC('localhost')
#esme.bind_SMSC()
#esme.disconnect_SMSC()


print ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>"

print "\n==============================================================="
test_bin = binascii.a2b_hex(re.sub(' ','','00 00 00 3C 00 00 00 04 00 00 00 00 00 00 00 05 00 02 08 35 35 35 00 01 01 35 35 35 35 35 35 35 35 35 00 00 00 00 00 00 00 00 00 00 0F 48 65 6C 6C 6F 20 77 69 6B 69 70 65 64 69 61 00000000 001d00026566'))
print json.dumps(unpack_pdu(test_bin), indent=4, sort_keys=True)

print "\n==============================================================="
test_bin = binascii.a2b_hex(re.sub(' ','','00000000 00000021 00000000 00000000 00 00 00 00 02 0101016500 026600 00 00 00 00 00 00 00 00 00 00 000500020000 0000000400000000'))
print json.dumps(unpack_pdu(test_bin), indent=4, sort_keys=True)

print "\n==============================================================="
test_bin = binascii.a2b_hex(re.sub(' ','','00000000 80000021 00000000 00000000 00 02 01016565650000000000 01016666660000000000'))
print json.dumps(unpack_pdu(test_bin), indent=4, sort_keys=True)

print "\n==============================================================="
test_bin = pack_pdu('generic_nack','ESME_ROK',1,'001d000b6162636465666768696a6b')
print json.dumps(unpack_pdu(test_bin), indent=4, sort_keys=True)

print "\n==============================================================="
test_bin = pack_pdu()
print json.dumps(unpack_pdu(test_bin), indent=4, sort_keys=True)


j = {
    'header': {
        'command_length': 16,
        'command_id': 'bind_transmitter',
        'command_status': 'ESME_ROK',
        'sequence_number': 0
    },
    'body': {
        'optional_parameters': [
            {
                'tag':'payload_type',
                'value':0
            }
        ]
    }
}

json_to_pdu(j)
