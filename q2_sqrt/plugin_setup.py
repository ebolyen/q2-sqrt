from qiime2.plugin import Plugin, SemanticType

from q2_types.feature_table import FeatureTable, RelativeFrequency, BIOMV210DirFmt

from q2_sqrt.action import square_root

plugin = Plugin("sqrt", version="0.0.1.dev", website="google.com",
                package="q2_sqrt")


SquareRoot = SemanticType('SquareRoot', variant_of=FeatureTable.field['content'])


plugin.register_semantic_types(SquareRoot)

plugin.register_semantic_type_to_format(FeatureTable[SquareRoot], BIOMV210DirFmt)

plugin.methods.register_function(
    square_root,
    name="Square Root Transform",
    description="Convert a table from relative frequency to square root",
    inputs={
        "table": FeatureTable[RelativeFrequency]
    },
    parameters={},
    outputs=[
        ("sqrt_table", FeatureTable[SquareRoot])
    ],
    input_descriptions={
        "table": "A relative frequency table"
    },
    output_descriptions={
        'sqrt_table': 'The transformed table'
    })

