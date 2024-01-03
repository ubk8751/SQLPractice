import sqlite3

def create_table(conn, table_name, col_dict):
    query = f'CREATE TABLE {table_name} (\n'
    for key in col_dict.keys():
        query += f'{key} {col_dict[key]},\n'
    query = query.rstrip(',\n')
    query += '\n)'
    conn.execute(query)

def insert_into_table(conn, table_name, col_names, data):
    placeholders = ', '.join(['?' for _ in col_names])
    query = f'INSERT INTO {table_name} ({", ".join(col_names)}) VALUES ({placeholders})'
    conn.executemany(query, data)

