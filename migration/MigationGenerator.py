from datetime import datetime
import os
import sys

up_template = """create table {0} (
    id number(19, 0) not null,
    created_at timestamp null,
    updated_at timestamp null,
    constraint {0}_id_pk primary key (id)
);

create sequence {0}_id_seq minvalue 1 start with 1 increment by 1;

create trigger {0}_id_trg 
before insert on {0} 
for each row 
begin 
if :new.ID is null then select {0}_id_seq.nextval into :new.ID from dual; 
end if;
end;
/
"""

down_template = """DROP TABLE {0};

DROP SEQUENCE {0}_id_seq;
"""

class MigrationGenerator():
    
    def get_dir(self, name):
        dir = os.path.dirname(os.path.realpath(sys.argv[0])) + f'/sql'
        now = datetime.now()
        formatted = now.strftime("%Y_%m_%d_%H%M%S")
        return f'{dir}/{formatted}_{name}'
    
    def generate_migration(self, name, table = None):
        dir = self.get_dir(name)
        os.mkdir(dir)
        
        if(table == None):
            os.mknod(f'{dir}/up.sql')
            os.mknod(f'{dir}/down.sql')
        else:
            with open(f'{dir}/up.sql', "w") as text_file:
                text_file.write(up_template.format(table))
            with open(f'{dir}/down.sql', "w") as text_file:
                text_file.write(down_template.format(table))
