"""
Fortran 2003 syntax
"""

import fparser.Fortran2003 as baseparser



class ClassType(baseparser.ClassType):
  pass

class NoMatchError(Exception):
  pass

class ParseError(Exception):
  pass

class Base(object):
  pass

class BlockBase(Base):
  pass

class SequenceBase(Base):
  pass

class UnaryOpBase(Base):
  pass

class BinaryOpBase(Base):
  pass

class SeparatorBase(Base):
  pass

class KeywordValueBase(Base):
  pass

class BracketBase(Base):
  pass

class NumberBase(Base):
  pass

class CallBase(Base):
  pass

class CALLBase(CallBase):
  pass

class StringBase(Base):
  pass

class STRINGBase(StringBase):
  pass

class StmtBase(Base):
  pass

class EndStmtBase(StmtBase):
  pass

class WORDClsBase(Base):
  pass

class Type_Declaration_StmtBase(StmtBase):
  pass

class Program(BlockBase): # R201
  pass

class Program_Unit(Base): # R202
  pass

class External_Subprogram(Base): # R203
  pass

class Specification_Part(BlockBase): # R204
  pass

class Implicit_Part(BlockBase): # R205
  pass

class Implicit_Part_Stmt(Base): # R206
  pass

class Declaration_Construct(Base): # R207
  pass

class Execution_Part(BlockBase): # R208
  pass

class Execution_Part_Construct(Base): # R209
  pass

class Execution_Part_Construct_C201(Base):
  pass

class Internal_Subprogram_Part(BlockBase): # R210
  pass

class Internal_Subprogram(Base): # R211
  pass

class Specification_Stmt(Base):# R212
  pass

class Executable_Construct(Base):# R213
  pass

class Executable_Construct_C201(Base):
  pass

class Action_Stmt(Base):# R214
  pass

class Action_Stmt_C201(Base):
  pass

class Action_Stmt_C802(Base):
  pass

class Action_Stmt_C824(Base):
  pass

class Keyword(Base): # R215
  pass

class Name(StringBase): # R304
  pass

class Constant(Base): # R305
  pass

class Literal_Constant(Base): # R306
  pass

class Named_Constant(Base): # R307
  pass

class Int_Constant(Base): # R308
  pass

class Char_Constant(Base): # R309
  pass

class Label(StringBase): # R313
  pass

class Type_Spec(Base): # R401
  pass

class Type_Param_Value(StringBase): # R402
  pass

class Intrinsic_Type_Spec(WORDClsBase): # R403
  pass

class Kind_Selector(Base): # R404
  pass

class Signed_Int_Literal_Constant(NumberBase): # R405
  pass

class Int_Literal_Constant(NumberBase): # R406
  pass

class Digit_String(NumberBase):
  pass

class Boz_Literal_Constant(Base): # R411
  pass

class Binary_Constant(STRINGBase): # R412
  pass

class Octal_Constant(STRINGBase): # R413
  pass

class Hex_Constant(STRINGBase): # R414
  pass

class Signed_Real_Literal_Constant(NumberBase): # R416
  pass

class Real_Literal_Constant(NumberBase): # R417
  pass

class Complex_Literal_Constant(Base): # R421
  pass

class Real_Part(Base): # R422
  pass

class Imag_Part(Base): # R423
  pass

class Char_Selector(Base): # R424
  pass

class Length_Selector(Base): # R425
  pass

class Char_Length(BracketBase): # R426
  pass

class Char_Literal_Constant(Base): # R427
  pass

class Logical_Literal_Constant(NumberBase): # R428
  pass

class Derived_Type_Def(BlockBase): # R429
  pass

class Derived_Type_Stmt(StmtBase): # R430
  pass

class Type_Name(Name): # C424
  pass

class Type_Attr_Spec(Base): # R431
  pass

class Private_Or_Sequence(Base): # R432
  pass

class End_Type_Stmt(EndStmtBase): # R433
  pass

class Sequence_Stmt(STRINGBase): # R434
  pass

class Type_Param_Def_Stmt(StmtBase): # R435
  pass

class Type_Param_Decl(BinaryOpBase): # R436
  pass

class Type_Param_Attr_Spec(STRINGBase): # R437
  pass

class Component_Part(BlockBase): # R438
  pass

class Component_Def_Stmt(Base): # R439
  pass

class Data_Component_Def_Stmt(Type_Declaration_StmtBase): # R440
  pass

class Dimension_Component_Attr_Spec(CALLBase):
  pass

class Component_Attr_Spec(STRINGBase): # R441
  pass

class Component_Decl(Base): # R442
  pass

class Component_Array_Spec(Base): # R443
  pass

class Component_Initialization(Base): # R444
  pass

class Proc_Component_Def_Stmt(StmtBase): # R445
  pass

class Proc_Component_PASS_Arg_Name(CALLBase):
  pass

class Proc_Component_Attr_Spec(STRINGBase): # R446
  pass

class Private_Components_Stmt(StmtBase): # R447
  pass

class Type_Bound_Procedure_Part(BlockBase): # R448
  pass

class Binding_Private_Stmt(StmtBase, STRINGBase): # R449
  pass

class Proc_Binding_Stmt(Base): # R450
  pass

class Specific_Binding(StmtBase): # R451
  pass

class Generic_Binding(StmtBase): # R452
  pass

class Binding_PASS_Arg_Name(CALLBase):
  pass

class Binding_Attr(STRINGBase): # R453
  pass

class Final_Binding(StmtBase, WORDClsBase): # R454
  pass

class Derived_Type_Spec(CallBase): # R455
  pass

class Type_Param_Spec(KeywordValueBase): # R456
  pass

class Structure_Constructor_2(KeywordValueBase): # R457.b
  pass

class Structure_Constructor(CallBase): # R457
  pass

class Component_Spec(KeywordValueBase): # R458
  pass

class Component_Data_Source(Base): # R459
  pass

class Enum_Def(BlockBase): # R460
  pass

class Enum_Def_Stmt(StmtBase): # R461
  pass

class Enumerator_Def_Stmt(StmtBase, WORDClsBase): # R462
  pass

class Enumerator(BinaryOpBase): # R463
  pass

class End_Enum_Stmt(EndStmtBase): # R464
  pass

class Array_Constructor(BracketBase): # R465
  pass

class Ac_Spec(Base): # R466
  pass

class Ac_Value(Base): # R469
  pass

class Ac_Implied_Do(Base): # R470
  pass

class Ac_Implied_Do_Control(Base): # R471
  pass

class Ac_Do_Variable(Base): # R472
  pass

class Type_Declaration_Stmt(Type_Declaration_StmtBase): # R501
  pass

class Declaration_Type_Spec(Base): # R502
  pass

class Dimension_Attr_Spec(CALLBase): # R503.d
  pass

class Intent_Attr_Spec(CALLBase): # R503.f
  pass

class Attr_Spec(STRINGBase): # R503
  pass

class Entity_Decl(Base): # R504
  pass

class Object_Name(Base): # R505
  pass

class Initialization(Base): # R506
  pass

class Null_Init(STRINGBase): # R507
  pass

class Access_Spec(STRINGBase): # R508
  pass

class Language_Binding_Spec(Base): # R509
  pass

class Array_Spec(Base): # R510
  pass

class Explicit_Shape_Spec(SeparatorBase): # R511
  pass

class Lower_Bound(Base): # R512
  pass

class Upper_Bound(Base): # R513
  pass

class Assumed_Shape_Spec(SeparatorBase): # R514
  pass

class Deferred_Shape_Spec(SeparatorBase): # R515
  pass

class Assumed_Size_Spec(Base): # R516
  pass

class Intent_Spec(STRINGBase): # R517
  pass

class Access_Stmt(StmtBase, WORDClsBase): # R518
  pass

class Access_Id(Base): # R519
  pass

class Object_Name_Deferred_Shape_Spec_List_Item(CallBase):
  pass

class Allocatable_Stmt(StmtBase, WORDClsBase): # R520
  pass

class Asynchronous_Stmt(StmtBase, WORDClsBase): # R521
  pass

class Bind_Stmt(StmtBase): # R522
  pass

class Bind_Entity(BracketBase): # R523
  pass

class Data_Stmt(StmtBase): # R524
  pass

class Data_Stmt_Set(Base): # R525
  pass

class Data_Stmt_Object(Base): # R526
  pass

class Data_Implied_Do(Base): # R527
  pass

class Data_I_Do_Object(Base): # R528
  pass

class Data_I_Do_Variable(Base): # R529
  pass

class Data_Stmt_Value(Base): # R530
  pass

class Data_Stmt_Repeat(Base): # R531
  pass

class Data_Stmt_Constant(Base): # R532
  pass

class Int_Constant_Subobject(Base): # R533
  pass

class Constant_Subobject(Base): # R534
  pass

class Dimension_Stmt(StmtBase): # R535
  pass

class Intent_Stmt(StmtBase): # R536
  pass

class Optional_Stmt(StmtBase, WORDClsBase): # R537
  pass

class Parameter_Stmt(StmtBase, CALLBase): # R538
  pass

class Named_Constant_Def(KeywordValueBase): # R539
  pass

class Pointer_Stmt(StmtBase, WORDClsBase): # R540
  pass

class Pointer_Decl(CallBase): # R541
  pass

class Protected_Stmt(StmtBase, WORDClsBase): # R542
  pass

class Save_Stmt(StmtBase, WORDClsBase): # R543
  pass

class Saved_Entity(BracketBase): # R544
  pass

class Proc_Pointer_Name(Base): # R545
  pass

class Target_Entity_Decl(Entity_Decl):
  pass

class Target_Stmt(StmtBase): # R546
  pass

class Value_Stmt(StmtBase, WORDClsBase): # R547
  pass

class Volatile_Stmt(StmtBase, WORDClsBase): # R548
  pass

class Implicit_Stmt(StmtBase): # R549
  pass

class Implicit_Spec(CallBase): # R550
  pass

class Letter_Spec(Base): # R551
  pass

class Namelist_Stmt(StmtBase): # R552
  pass

class Namelist_Group_Object(Base): # R553
  pass

class Equivalence_Stmt(StmtBase, WORDClsBase): # R554
  pass

class Equivalence_Set(Base): # R555
  pass

class Equivalence_Object(Base): # R556
  pass

class Common_Stmt(StmtBase): # R557
  pass

class Common_Block_Object(CallBase): # R558
  pass

class Variable(Base): # R601
  pass

class Variable_Name(Base): # R602
  pass

class Designator(Base): # R603
  pass

class Logical_Variable(Base): # R604
  pass

class Default_Logical_Variable(Base): # R605
  pass

class Char_Variable(Base): # R606
  pass

class Default_Char_Variable(Base): # R607
  pass

class Int_Variable(Base): # R608
  pass

class Substring(CallBase): # R609
  pass

class Parent_String(Base): # R610
  pass

class Substring_Range(SeparatorBase): # R611
  pass

class Data_Ref(SequenceBase): # R612
  pass

class Part_Ref(CallBase): # R613
  pass

class Structure_Component(Base): # R614
  pass

class Type_Param_Inquiry(BinaryOpBase): # R615
  pass

class Array_Element(Base): # R616
  pass

class Array_Section(CallBase): # R617
  pass

class Subscript(Base): # R618
  pass

class Section_Subscript(Base): # R619
  pass

class Subscript_Triplet(Base): # R620
  pass

class Stride(Base): # R621
  pass

class Vector_Subscript(Base): # R622
  pass

class Allocate_Stmt(StmtBase): # R623
  pass

class Alloc_Opt(KeywordValueBase):# R624
  pass

class Stat_Variable(Base):# R625
  pass

class Errmsg_Variable(Base):# R626
  pass

class Source_Expr(Base):# R627
  pass

class Allocation(CallBase):# R628
  pass

class Allocate_Object(Base): # R629
  pass

class Allocate_Shape_Spec(SeparatorBase): # R630
  pass

class Lower_Bound_Expr(Base): # R631
  pass

class Upper_Bound_Expr(Base): # R632
  pass

class Nullify_Stmt(StmtBase, CALLBase): # R633
  pass

class Pointer_Object(Base): # R634
  pass

class Deallocate_Stmt(StmtBase): # R635
  pass

class Dealloc_Opt(KeywordValueBase): # R636
  pass

class Scalar_Char_Initialization_Expr(Base):
  pass

class Primary(Base): # R701
  pass

class Parenthesis(BracketBase): # R701.h
  pass

class Level_1_Expr(UnaryOpBase): # R702
  pass

class Defined_Unary_Op(STRINGBase): # R703
  pass

class Defined_Op(STRINGBase): # R703, 723
  pass

class Mult_Operand(BinaryOpBase): # R704
  pass

class Add_Operand(BinaryOpBase): # R705
  pass

class Level_2_Expr(BinaryOpBase): # R706
  pass

class Level_2_Unary_Expr(UnaryOpBase): # R706.c
  pass

class Level_3_Expr(BinaryOpBase): # R710
  pass

class Level_4_Expr(BinaryOpBase): # R712
  pass

class And_Operand(UnaryOpBase): # R714
  pass

class Or_Operand(BinaryOpBase): # R715
  pass

class Equiv_Operand(BinaryOpBase): # R716
  pass

class Level_5_Expr(BinaryOpBase): # R717
  pass

class Expr(BinaryOpBase): # R722
  pass

class Defined_Unary_Op(STRINGBase): # R723
  pass

class Logical_Expr(Base): # R724
  pass

class Char_Expr(Base): # R725
  pass

class Default_Char_Expr(Base): # R726
  pass

class Int_Expr(Base): # R727
  pass

class Numeric_Expr(Base): # R728
  pass

class Specification_Expr(Base): # R729
  pass

class Initialization_Expr(Base): # R730
  pass

class Char_Initialization_Expr(Base): # R731
  pass

class Int_Initialization_Expr(Base): # R732
  pass

class Logical_Initialization_Expr(Base): # R733
  pass

class Assignment_Stmt(StmtBase, BinaryOpBase): # R734
  pass

class Pointer_Assignment_Stmt(StmtBase): # R735
  pass

class Data_Pointer_Object(BinaryOpBase): # R736
  pass

class Bounds_Spec(SeparatorBase): # R737
  pass

class Bounds_Remapping(SeparatorBase): # R738
  pass

class Data_Target(Base): # R739
  pass

class Proc_Pointer_Object(Base): # R740
  pass

class Proc_Component_Ref(BinaryOpBase): # R741
  pass

class Proc_Target(Base): # R742
  pass

class Where_Stmt(StmtBase): # R743
  pass

class Where_Construct(BlockBase): # R744
  pass

class Where_Construct_Stmt(StmtBase): # R745
  pass

class Where_Body_Construct(Base): # R746
  pass

class Where_Assignment_Stmt(Base): # R747
  pass

class Mask_Expr(Base): # R748
  pass

class Masked_Elsewhere_Stmt(StmtBase): # R749
  pass

class Elsewhere_Stmt(StmtBase, WORDClsBase): # R750
  pass

class End_Where_Stmt(EndStmtBase): # R751
  pass

class Forall_Construct(BlockBase): # R752
  pass

class Forall_Construct_Stmt(StmtBase, WORDClsBase): # R753
  pass

class Forall_Header(Base): # R754
  pass

class Forall_Triplet_Spec(Base): # R755
  pass

class Forall_Body_Construct(Base): # R756
  pass

class Forall_Assignment_Stmt(Base): # R757
  pass

class End_Forall_Stmt(EndStmtBase): # R758
  pass

class Forall_Stmt(StmtBase): # R759
  pass

class Block(BlockBase): # R801
  pass

class If_Construct(BlockBase): # R802
  pass

class If_Then_Stmt(StmtBase): # R803
  pass

class Else_If_Stmt(StmtBase): # R804
  pass

class Else_Stmt(StmtBase): # R805
  pass

class End_If_Stmt(EndStmtBase): # R806
  pass

class If_Stmt(StmtBase): # R807
  pass

class Case_Construct(BlockBase): # R808
  pass

class Select_Case_Stmt(StmtBase, CALLBase): # R809
  pass

class Case_Stmt(StmtBase): # R810
  pass

class End_Select_Stmt(EndStmtBase): # R811
  pass

class Case_Expr(Base): # R812
  pass

class Case_Selector(Base): # R813
  pass

class Case_Value_Range(SeparatorBase): # R814
  pass

class Case_Value(Base): # R815
  pass

class Associate_Construct(BlockBase): # R816
  pass

class Associate_Stmt(StmtBase, CALLBase): # R817
  pass

class Association(BinaryOpBase): # R818
  pass

class Selector(Base): # R819
  pass

class End_Associate_Stmt(EndStmtBase): # R820
  pass

class Select_Type_Construct(BlockBase): # R821
  pass

class Select_Type_Stmt(StmtBase): # R822
  pass

class Type_Guard_Stmt(StmtBase): # R823
  pass

class End_Select_Type_Stmt(EndStmtBase): # R824
  pass

class Do_Construct(Base): # R825
  pass

class Block_Do_Construct(Base): # R826
  pass

class Block_Label_Do_Construct(BlockBase): # R826_1
  pass

class Block_Nonlabel_Do_Construct(BlockBase): # R826_2
  pass

class Do_Stmt(Base): # R827
  pass

class Label_Do_Stmt(StmtBase): # R828
  pass

class Nonlabel_Do_Stmt(StmtBase, WORDClsBase): # R829
  pass

class Loop_Control(Base): # R830
  pass

class Do_Variable(Base): # R831
  pass

class Do_Block(BlockBase): # R832
  pass

class End_Do(Base): # R833
  pass

class End_Do_Stmt(EndStmtBase): # R834
  pass

class Nonblock_Do_Construct(Base): # R835
  pass

class Action_Term_Do_Construct(BlockBase): # R836
  pass

class Do_Body(BlockBase): # R837
  pass

class Do_Term_Action_Stmt(StmtBase): # R838
  pass

class Outer_Shared_Do_Construct(BlockBase): # R839
  pass

class Shared_Term_Do_Construct(Base): # R840
  pass

class Inner_Shared_Do_Construct(BlockBase): # R841
  pass

class Do_Term_Shared_Stmt(StmtBase): # R842
  pass

class Cycle_Stmt(StmtBase, WORDClsBase): # R843
  pass

class Exit_Stmt(StmtBase, WORDClsBase): # R844
  pass

class Goto_Stmt(StmtBase): # R845
  pass

class Computed_Goto_Stmt(StmtBase): # R846
  pass

class Arithmetic_If_Stmt(StmtBase): # R847
  pass

class Continue_Stmt(StmtBase, STRINGBase): # R848
  pass

class Stop_Stmt(StmtBase, WORDClsBase): # R849
  pass

class Stop_Code(StringBase): # R850
  pass

class Io_Unit(StringBase): # R901
  pass

class File_Unit_Number(Base): # R902
  pass

class Internal_File_Variable(Base): # R903
  pass

class Open_Stmt(StmtBase, CALLBase): # R904
  pass

class Connect_Spec(KeywordValueBase): # R905
  pass

class File_Name_Expr(Base): # R906
  pass

class Iomsg_Variable(Base): # R907
  pass

class Close_Stmt(StmtBase, CALLBase): # R908
  pass

class Close_Spec(KeywordValueBase): # R909
  pass

class Read_Stmt(StmtBase): # R910
  pass

class Write_Stmt(StmtBase): # R911
  pass

class Print_Stmt(StmtBase): # R912
  pass

class Io_Control_Spec_List(SequenceBase): # R913-list
  pass

class Io_Control_Spec(KeywordValueBase): # R913
  pass

class Format(StringBase): # R914
  pass

class Input_Item(Base): # R915
  pass

class Output_Item(Base): # R916
  pass

class Io_Implied_Do(Base): # R917
  pass

class Io_Implied_Do_Object(Base): # R918
  pass

class Io_Implied_Do_Control(Base): # R919
  pass

class Dtv_Type_Spec(CALLBase): # R920
  pass

class Wait_Stmt(StmtBase, CALLBase): # R921
  pass

class Wait_Spec(KeywordValueBase): # R922
  pass

class Backspace_Stmt(StmtBase): # R923
  pass

class Endfile_Stmt(StmtBase): # R924
  pass

class Rewind_Stmt(StmtBase): # R925
  pass

class Position_Spec(KeywordValueBase): # R926
  pass

class Flush_Stmt(StmtBase): # R927
  pass

class Flush_Spec(KeywordValueBase): # R928
  pass

class Inquire_Stmt(StmtBase): # R929
  pass

class Inquire_Spec(KeywordValueBase): # R930
  pass

class Format_Stmt(StmtBase, WORDClsBase): # R1001
  pass

class Format_Specification(BracketBase): # R1002
  pass

class Format_Item_C1002(Base): # C1002
  pass

class Format_Item(Base): # R1003
  pass

class R(Base): # R1004
  pass

class Data_Edit_Desc_C1002(Base):
  pass

class Data_Edit_Desc(Base): # R1005
  pass

class W(Base): # R1006
  pass

class M(Base): # R1007
  pass

class D(Base): # R1008
  pass

class E(Base): # R1009
  pass

class V(Base): # R1010
  pass

class Control_Edit_Desc(Base): # R1011
  pass

class K(Base): # R1012
  pass

class Position_Edit_Desc(Base): # R1013
  pass

class N(Base): # R1014
  pass

class Sign_Edit_Desc(STRINGBase): # R1015
  pass

class Blank_Interp_Edit_Desc(STRINGBase): # R1016
  pass

class Round_Edit_Desc(STRINGBase): # R1017
  pass

class Decimal_Edit_Desc(STRINGBase): # R1018
  pass

class Char_String_Edit_Desc(Base): # R1019
  pass

class Main_Program(BlockBase): # R1101
  pass

class Main_Program0(BlockBase):
  pass

class Program_Stmt(StmtBase, WORDClsBase): # R1102
  pass

class End_Program_Stmt(EndStmtBase): # R1103
  pass

class Module(BlockBase): # R1104
  pass

class Module_Stmt(StmtBase, WORDClsBase): # R1105
  pass

class End_Module_Stmt(EndStmtBase): # R1106
  pass

class Module_Subprogram_Part(BlockBase): # R1107
  pass

class Module_Subprogram(Base): # R1108
  pass

class Use_Stmt(StmtBase): # R1109
  pass

class Module_Nature(STRINGBase): # R1110
  pass

class Rename(Base): # R1111
  pass

class Only(Base): # R1112
  pass

class Only_Use_Name(Base): # R1113
  pass

class Local_Defined_Operator(Base): # R1114
  pass

class Use_Defined_Operator(Base): # R1115
  pass

class Block_Data(BlockBase): # R1116
  pass

class Block_Data_Stmt(StmtBase): # R1117
  pass

class End_Block_Data_Stmt(EndStmtBase): # R1118
  pass

class Interface_Block(BlockBase): # R1201
  pass

class Interface_Specification(Base): # R1202
  pass

class Interface_Stmt(StmtBase): # R1203
  pass

class End_Interface_Stmt(EndStmtBase): # R1204
  pass

class Function_Body(BlockBase):
  pass

class Subroutine_Body(BlockBase):
  pass

class Interface_Body(Base): # R1205
  pass

class Procedure_Stmt(StmtBase): # R1206
  pass

class Generic_Spec(Base): # R1207
  pass

class Dtio_Generic_Spec(Base): # R1208
  pass

class Import_Stmt(StmtBase, WORDClsBase): # R1209
  pass

class External_Stmt(StmtBase, WORDClsBase): # R1210
  pass

class Procedure_Declaration_Stmt(StmtBase): # R1211
  pass

class Proc_Interface(Base): # R1212
  pass

class Proc_Attr_Spec(Base): # R1213
  pass

class Proc_Decl(BinaryOpBase): # R1214
  pass

class Interface_Name(Base): # R1215
  pass

class Intrinsic_Stmt(StmtBase, WORDClsBase): # R1216
  pass

class Function_Reference(CallBase): # R1217
  pass

class Call_Stmt(StmtBase): # R1218
  pass

class Procedure_Designator(BinaryOpBase): # R1219
  pass

class Actual_Arg_Spec(KeywordValueBase): # R1220
  pass

class Actual_Arg(Base): # R1221
  pass

class Alt_Return_Spec(Base): # R1222
  pass

class Function_Subprogram(BlockBase): # R1223
  pass

class Function_Stmt(StmtBase): # R1224
  pass

class Proc_Language_Binding_Spec(Base): #1225
  pass

class Dummy_Arg_Name(Base): # R1226
  pass

class Prefix(SequenceBase): # R1227
  pass

class Prefix_Spec(STRINGBase): # R1228
  pass

class Suffix(Base): # R1229
  pass

class End_Function_Stmt(EndStmtBase): # R1230
  pass

class Subroutine_Subprogram(BlockBase): # R1231
  pass

class Subroutine_Stmt(StmtBase): # R1232
  pass

class Dummy_Arg(StringBase): # R1233
  pass

class End_Subroutine_Stmt(EndStmtBase): # R1234
  pass

class Entry_Stmt(StmtBase): # R1235
  pass

class Return_Stmt(StmtBase): # R1236
  pass

class Contains_Stmt(StmtBase, STRINGBase): # R1237
  pass

class Stmt_Function_Stmt(StmtBase): # R1238
  pass

