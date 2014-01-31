#Reference: fedmsg.com/en/latest/consuming

import fedmsg

config = fedmsg.config.load_config([], None)

config['mute'] = True

config['timeout'] = 0

for name, endpoint, topic, msg in fedmsg.tail_messages(**config):
    if topic.find('org.fedoraproject.prod.git') != -1:
        print "Fedora Project Git accessed" 
        print topic
    if topic.find('build') != -1:
        print "Build event occured"
        print topic
    #print topic, fedmsg.encoding.pretty_dumps(msg)
