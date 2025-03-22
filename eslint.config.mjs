import stylisticJs from '@stylistic/eslint-plugin-js';

export default [
    {
        plugins: {
            '@stylistic/js': stylisticJs
        },
        rules: {
            '@stylistic/js/indent': ['error', 4],
            '@stylistic/js/semi': ['warn', 'always'],
            '@stylistic/js/quotes': ['error', 'single'],
            '@stylistic/js/no-trailing-spaces': ['error'],
            '@stylistic/js/brace-style': ['error', '1tbs'],
            '@stylistic/js/no-tabs': ['error'],
            '@stylistic/js/space-before-function-paren': ['error', 'never'],
            '@stylistic/js/array-bracket-spacing': ['error', 'never'],
            '@stylistic/js/block-spacing': ['error', 'always'],
            '@stylistic/js/comma-spacing': ['error', { 'before': false, 'after': true }],
            '@stylistic/js/key-spacing': ['error', { 'beforeColon': false, 'afterColon': true }],
            '@stylistic/js/space-in-parens': ['error', 'never'],
            '@stylistic/js/space-infix-ops': ['error', { 'int32Hint': false }]
        }
    }
];
