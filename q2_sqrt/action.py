import biom

def square_root(table: biom.Table) -> biom.Table:
    return biom.Table(table.matrix_data.sqrt(),
                      table.ids('observation'), table.ids('sample'))
