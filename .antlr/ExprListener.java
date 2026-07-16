// Generated from c:/Users/joseb/Music/proyecto_profecional/Expr.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link ExprParser}.
 */
public interface ExprListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link ExprParser#root}.
	 * @param ctx the parse tree
	 */
	void enterRoot(ExprParser.RootContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#root}.
	 * @param ctx the parse tree
	 */
	void exitRoot(ExprParser.RootContext ctx);
	/**
	 * Enter a parse tree produced by the {@code functionDecl}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterFunctionDecl(ExprParser.FunctionDeclContext ctx);
	/**
	 * Exit a parse tree produced by the {@code functionDecl}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitFunctionDecl(ExprParser.FunctionDeclContext ctx);
	/**
	 * Enter a parse tree produced by the {@code newExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterNewExpr(ExprParser.NewExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code newExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitNewExpr(ExprParser.NewExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code assignmentExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentExpr(ExprParser.AssignmentExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code assignmentExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentExpr(ExprParser.AssignmentExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code debuggerExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterDebuggerExpr(ExprParser.DebuggerExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code debuggerExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitDebuggerExpr(ExprParser.DebuggerExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code multiplicative}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterMultiplicative(ExprParser.MultiplicativeContext ctx);
	/**
	 * Exit a parse tree produced by the {@code multiplicative}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitMultiplicative(ExprParser.MultiplicativeContext ctx);
	/**
	 * Enter a parse tree produced by the {@code breakExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterBreakExpr(ExprParser.BreakExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code breakExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitBreakExpr(ExprParser.BreakExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code forInExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterForInExpr(ExprParser.ForInExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code forInExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitForInExpr(ExprParser.ForInExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code switchExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterSwitchExpr(ExprParser.SwitchExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code switchExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitSwitchExpr(ExprParser.SwitchExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code postIncDec}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterPostIncDec(ExprParser.PostIncDecContext ctx);
	/**
	 * Exit a parse tree produced by the {@code postIncDec}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitPostIncDec(ExprParser.PostIncDecContext ctx);
	/**
	 * Enter a parse tree produced by the {@code forExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterForExpr(ExprParser.ForExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code forExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitForExpr(ExprParser.ForExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code unaryExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterUnaryExpr(ExprParser.UnaryExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code unaryExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitUnaryExpr(ExprParser.UnaryExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code nullishExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterNullishExpr(ExprParser.NullishExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code nullishExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitNullishExpr(ExprParser.NullishExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code ifExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterIfExpr(ExprParser.IfExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code ifExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitIfExpr(ExprParser.IfExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code blockExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterBlockExpr(ExprParser.BlockExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code blockExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitBlockExpr(ExprParser.BlockExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code importExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterImportExpr(ExprParser.ImportExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code importExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitImportExpr(ExprParser.ImportExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code callExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterCallExpr(ExprParser.CallExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code callExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitCallExpr(ExprParser.CallExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code equality}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterEquality(ExprParser.EqualityContext ctx);
	/**
	 * Exit a parse tree produced by the {@code equality}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitEquality(ExprParser.EqualityContext ctx);
	/**
	 * Enter a parse tree produced by the {@code preIncDec}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterPreIncDec(ExprParser.PreIncDecContext ctx);
	/**
	 * Exit a parse tree produced by the {@code preIncDec}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitPreIncDec(ExprParser.PreIncDecContext ctx);
	/**
	 * Enter a parse tree produced by the {@code conditionalExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterConditionalExpr(ExprParser.ConditionalExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code conditionalExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitConditionalExpr(ExprParser.ConditionalExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code throwExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterThrowExpr(ExprParser.ThrowExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code throwExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitThrowExpr(ExprParser.ThrowExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code memberAccess}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterMemberAccess(ExprParser.MemberAccessContext ctx);
	/**
	 * Exit a parse tree produced by the {@code memberAccess}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitMemberAccess(ExprParser.MemberAccessContext ctx);
	/**
	 * Enter a parse tree produced by the {@code exponentExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExponentExpr(ExprParser.ExponentExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code exponentExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExponentExpr(ExprParser.ExponentExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code classDecl}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterClassDecl(ExprParser.ClassDeclContext ctx);
	/**
	 * Exit a parse tree produced by the {@code classDecl}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitClassDecl(ExprParser.ClassDeclContext ctx);
	/**
	 * Enter a parse tree produced by the {@code doWhileExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterDoWhileExpr(ExprParser.DoWhileExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code doWhileExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitDoWhileExpr(ExprParser.DoWhileExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code returnExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterReturnExpr(ExprParser.ReturnExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code returnExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitReturnExpr(ExprParser.ReturnExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code logicalAnd}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterLogicalAnd(ExprParser.LogicalAndContext ctx);
	/**
	 * Exit a parse tree produced by the {@code logicalAnd}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitLogicalAnd(ExprParser.LogicalAndContext ctx);
	/**
	 * Enter a parse tree produced by the {@code arrowFunction}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterArrowFunction(ExprParser.ArrowFunctionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code arrowFunction}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitArrowFunction(ExprParser.ArrowFunctionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code awaitExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterAwaitExpr(ExprParser.AwaitExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code awaitExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitAwaitExpr(ExprParser.AwaitExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code forOfExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterForOfExpr(ExprParser.ForOfExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code forOfExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitForOfExpr(ExprParser.ForOfExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code additive}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterAdditive(ExprParser.AdditiveContext ctx);
	/**
	 * Exit a parse tree produced by the {@code additive}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitAdditive(ExprParser.AdditiveContext ctx);
	/**
	 * Enter a parse tree produced by the {@code indexAccess}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterIndexAccess(ExprParser.IndexAccessContext ctx);
	/**
	 * Exit a parse tree produced by the {@code indexAccess}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitIndexAccess(ExprParser.IndexAccessContext ctx);
	/**
	 * Enter a parse tree produced by the {@code continueExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterContinueExpr(ExprParser.ContinueExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code continueExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitContinueExpr(ExprParser.ContinueExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code whileExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterWhileExpr(ExprParser.WhileExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code whileExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitWhileExpr(ExprParser.WhileExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code tryExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterTryExpr(ExprParser.TryExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code tryExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitTryExpr(ExprParser.TryExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code primaryS}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterPrimaryS(ExprParser.PrimarySContext ctx);
	/**
	 * Exit a parse tree produced by the {@code primaryS}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitPrimaryS(ExprParser.PrimarySContext ctx);
	/**
	 * Enter a parse tree produced by the {@code optionalChainExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterOptionalChainExpr(ExprParser.OptionalChainExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code optionalChainExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitOptionalChainExpr(ExprParser.OptionalChainExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code exportExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterExportExpr(ExprParser.ExportExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code exportExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitExportExpr(ExprParser.ExportExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code variableDecl}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterVariableDecl(ExprParser.VariableDeclContext ctx);
	/**
	 * Exit a parse tree produced by the {@code variableDecl}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitVariableDecl(ExprParser.VariableDeclContext ctx);
	/**
	 * Enter a parse tree produced by the {@code relational}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterRelational(ExprParser.RelationalContext ctx);
	/**
	 * Exit a parse tree produced by the {@code relational}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitRelational(ExprParser.RelationalContext ctx);
	/**
	 * Enter a parse tree produced by the {@code withExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterWithExpr(ExprParser.WithExprContext ctx);
	/**
	 * Exit a parse tree produced by the {@code withExpr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitWithExpr(ExprParser.WithExprContext ctx);
	/**
	 * Enter a parse tree produced by the {@code logicalOr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterLogicalOr(ExprParser.LogicalOrContext ctx);
	/**
	 * Exit a parse tree produced by the {@code logicalOr}
	 * labeled alternative in {@link ExprParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitLogicalOr(ExprParser.LogicalOrContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#variableModifier}.
	 * @param ctx the parse tree
	 */
	void enterVariableModifier(ExprParser.VariableModifierContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#variableModifier}.
	 * @param ctx the parse tree
	 */
	void exitVariableModifier(ExprParser.VariableModifierContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#assignmentOperator}.
	 * @param ctx the parse tree
	 */
	void enterAssignmentOperator(ExprParser.AssignmentOperatorContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#assignmentOperator}.
	 * @param ctx the parse tree
	 */
	void exitAssignmentOperator(ExprParser.AssignmentOperatorContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#arrowParams}.
	 * @param ctx the parse tree
	 */
	void enterArrowParams(ExprParser.ArrowParamsContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#arrowParams}.
	 * @param ctx the parse tree
	 */
	void exitArrowParams(ExprParser.ArrowParamsContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#paramList}.
	 * @param ctx the parse tree
	 */
	void enterParamList(ExprParser.ParamListContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#paramList}.
	 * @param ctx the parse tree
	 */
	void exitParamList(ExprParser.ParamListContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#param}.
	 * @param ctx the parse tree
	 */
	void enterParam(ExprParser.ParamContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#param}.
	 * @param ctx the parse tree
	 */
	void exitParam(ExprParser.ParamContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#classMember}.
	 * @param ctx the parse tree
	 */
	void enterClassMember(ExprParser.ClassMemberContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#classMember}.
	 * @param ctx the parse tree
	 */
	void exitClassMember(ExprParser.ClassMemberContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#methodDefinition}.
	 * @param ctx the parse tree
	 */
	void enterMethodDefinition(ExprParser.MethodDefinitionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#methodDefinition}.
	 * @param ctx the parse tree
	 */
	void exitMethodDefinition(ExprParser.MethodDefinitionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#fieldDefinition}.
	 * @param ctx the parse tree
	 */
	void enterFieldDefinition(ExprParser.FieldDefinitionContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#fieldDefinition}.
	 * @param ctx the parse tree
	 */
	void exitFieldDefinition(ExprParser.FieldDefinitionContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#propertyName}.
	 * @param ctx the parse tree
	 */
	void enterPropertyName(ExprParser.PropertyNameContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#propertyName}.
	 * @param ctx the parse tree
	 */
	void exitPropertyName(ExprParser.PropertyNameContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#caseClause}.
	 * @param ctx the parse tree
	 */
	void enterCaseClause(ExprParser.CaseClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#caseClause}.
	 * @param ctx the parse tree
	 */
	void exitCaseClause(ExprParser.CaseClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#defaultClause}.
	 * @param ctx the parse tree
	 */
	void enterDefaultClause(ExprParser.DefaultClauseContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#defaultClause}.
	 * @param ctx the parse tree
	 */
	void exitDefaultClause(ExprParser.DefaultClauseContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#forInit}.
	 * @param ctx the parse tree
	 */
	void enterForInit(ExprParser.ForInitContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#forInit}.
	 * @param ctx the parse tree
	 */
	void exitForInit(ExprParser.ForInitContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#forUpdate}.
	 * @param ctx the parse tree
	 */
	void enterForUpdate(ExprParser.ForUpdateContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#forUpdate}.
	 * @param ctx the parse tree
	 */
	void exitForUpdate(ExprParser.ForUpdateContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#argumentList}.
	 * @param ctx the parse tree
	 */
	void enterArgumentList(ExprParser.ArgumentListContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#argumentList}.
	 * @param ctx the parse tree
	 */
	void exitArgumentList(ExprParser.ArgumentListContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#argument}.
	 * @param ctx the parse tree
	 */
	void enterArgument(ExprParser.ArgumentContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#argument}.
	 * @param ctx the parse tree
	 */
	void exitArgument(ExprParser.ArgumentContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#primaryExpr}.
	 * @param ctx the parse tree
	 */
	void enterPrimaryExpr(ExprParser.PrimaryExprContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#primaryExpr}.
	 * @param ctx the parse tree
	 */
	void exitPrimaryExpr(ExprParser.PrimaryExprContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#literal}.
	 * @param ctx the parse tree
	 */
	void enterLiteral(ExprParser.LiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#literal}.
	 * @param ctx the parse tree
	 */
	void exitLiteral(ExprParser.LiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#arrayLiteral}.
	 * @param ctx the parse tree
	 */
	void enterArrayLiteral(ExprParser.ArrayLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#arrayLiteral}.
	 * @param ctx the parse tree
	 */
	void exitArrayLiteral(ExprParser.ArrayLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#elementList}.
	 * @param ctx the parse tree
	 */
	void enterElementList(ExprParser.ElementListContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#elementList}.
	 * @param ctx the parse tree
	 */
	void exitElementList(ExprParser.ElementListContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#elementItem}.
	 * @param ctx the parse tree
	 */
	void enterElementItem(ExprParser.ElementItemContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#elementItem}.
	 * @param ctx the parse tree
	 */
	void exitElementItem(ExprParser.ElementItemContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#objectLiteral}.
	 * @param ctx the parse tree
	 */
	void enterObjectLiteral(ExprParser.ObjectLiteralContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#objectLiteral}.
	 * @param ctx the parse tree
	 */
	void exitObjectLiteral(ExprParser.ObjectLiteralContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#propertyList}.
	 * @param ctx the parse tree
	 */
	void enterPropertyList(ExprParser.PropertyListContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#propertyList}.
	 * @param ctx the parse tree
	 */
	void exitPropertyList(ExprParser.PropertyListContext ctx);
	/**
	 * Enter a parse tree produced by {@link ExprParser#property}.
	 * @param ctx the parse tree
	 */
	void enterProperty(ExprParser.PropertyContext ctx);
	/**
	 * Exit a parse tree produced by {@link ExprParser#property}.
	 * @param ctx the parse tree
	 */
	void exitProperty(ExprParser.PropertyContext ctx);
}